import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
from PySide6.QtCore import QObject, Signal
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple
import tools.afcCalculationV2 as afcCalculation
import plotly_express as px
import pandas as pd
from flask import request



class Server(QObject):
    shut_down_signal = Signal()

    def __init__(self, port, filepath):
        super().__init__()
        self.port = port
        self.filepath = filepath
        self.out_recent = pd.DataFrame
        self.out_far = pd.DataFrame

        # external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
        # self.app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
        self.app = dash.Dash(__name__)
        self.appSetLayout()

    def run(self):
        self.app.run_server(debug=False, port=self.port)
        # run_simple('localhost', port=self.port, application=DispatcherMiddleware(self.app.server))
        print("服务器已运行")

    def appSetLayout(self):
        fig = self.generateGraphics()
        shut_down_signal = self.shut_down_signal

        self.app.layout = html.Div([
            # # represents the URL bar, doesn't render anything
            dcc.Location(id='url', refresh=False),
            html.Div(id='page-content'),
            dcc.Graph(figure=fig['近期进站清单']),
            dcc.Graph(figure=fig['远期进站清单']),
        ])

        @self.app.callback(dash.dependencies.Output('page-content', 'children'), [dash.dependencies.Input('url', 'pathname')])
        def display_page(pathname):
            if pathname == '/shutdown':
                shutdown()
                shut_down_signal.emit()
            return html.Div([
                html.H5('视图界面')
            ])

        def shutdown():
            func = request.environ.get('werkzeug.server.shutdown')
            if func is None:
                raise RuntimeError('Not running with the Werkzeug Server')
            func()

    def generateGraphics(self):
        """
        获取要展示的图表

        :return:
        """
        filepath = self.filepath

        # 提取近期远期以及手动调整表格的内容
        para, ridershipAddress = afcCalculation.loadParam(filepath)
        table_recent = afcCalculation.AFC_project(file_path=ridershipAddress, tab_names=["近期早高峰客流", "近期晚高峰客流"], parameter_list=para).run()
        table_far = afcCalculation.AFC_project(file_path=ridershipAddress, tab_names=["远期早高峰客流", "远期晚高峰客流"], parameter_list=para).run()
        manual_df_recent = afcCalculation.get_dataFrame('output_recent', filepath)
        if manual_df_recent is None:
            manual_df_recent = table_recent[3].copy()

        manual_df_far = afcCalculation.get_dataFrame('output_far', filepath)
        if manual_df_far is None:
            manual_df_far = table_far[3].copy()

        d0 = table_recent[0].index.to_series()
        d1 = table_recent[1]['MAX(C进)']
        d2 = table_recent[2]['进站检票机\n(MAX)']
        d3 = table_recent[3]['进站检票机']
        d4 = manual_df_recent['进站检票机']
        self.out_recent: pd.Dataframe = pd.concat([d0, d1, d2, d3, d4], axis=1, join="outer")
        self.out_recent.columns = ["车站名", "MAX(C进)", "进站检票机\n(MAX)", "进站检票机(计算值)", "进站检票机(提资值)"]

        d0 = table_far[0].index.to_series()
        d1 = table_far[1]['MAX(C进)']
        d2 = table_far[2]['进站检票机\n(MAX)']
        d3 = table_far[3]['进站检票机']
        d4 = manual_df_far['进站检票机']
        self.out_far: pd.Dataframe = pd.concat([d0, d1, d2, d3, d4], axis=1, join="outer")
        self.out_far.columns = ["车站名", "MAX(C进)", "进站检票机\n(MAX)", "进站检票机(计算值)", "进站检票机(提资值)"]

        fig1 = px.parallel_categories(self.out_recent)
        fig2 = px.parallel_categories(self.out_far)

        fig = {
            '近期进站清单': fig1,
            '远期进站清单': fig2,
        }

        return fig

if __name__ == "__main__":
    server = Server(8085, "/天津1号线/测试项目01.afc")
    server.run()