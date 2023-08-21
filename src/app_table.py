import dash_mantine_components as dmc
from dash import Dash

app = Dash(
    __name__,
    external_stylesheets=[
        # include google fonts
        "https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400;500;900&display=swap"
    ],
)

from dash import html
from dash import html, Output, Input, State, callback


style = {
    "border": f"1px solid {dmc.theme.DEFAULT_COLORS['indigo'][4]}",
    "textAlign": "center",
}

def create_table(df):
    columns, values = df.columns, df.values
    header = [html.Thead([html.Tr([html.Th(col) for col in columns])])]
    body = [html.Tbody([html.Tr([html.Td(cell,style = {
                'font_family': 'cursive',
                'font_size': '15px',
                'text_align': 'center'
            },) for cell in row]) for row in values])]
    table = dmc.Table(header + body)
    return table

import pandas as pd
# data = [{"col1":1,"col2":2},
#         {"col1":2,"col2":5},
#         {"col1":3,"col2":6},
#         ]
# df = pd.DataFrame(data).T

df=pd.read_csv("./data/mit-data.csv").T

df1=df[[0]]
df2=df[[1]]
df3=df[[2]]
df4=df[[3]]

print(df.index)

column_df = pd.DataFrame(df.index,columns=["Metric"])

print(column_df)

dmc_table = create_table(df)

dmc_table0 = create_table(column_df)
dmc_table1 = create_table(df1)
dmc_table2 = create_table(df2)
dmc_table3 = create_table(df3)
dmc_table4 = create_table(df4)

acc0=dmc.AccordionItem(
    [
        dmc.AccordionControl("DEPLOYMENT IMPACT - METRICS"),
        # dmc.AccordionPanel(
        #     "Configure temp appearance and behavior with vast amount of settings or overwrite any part of "
        #     # "component styles "
        # ),
        dmc_table0
    ],
    value="flexibility0",
)
acc1=dmc.AccordionItem(
    [
        dmc.AccordionControl("Flexibility"),
        dmc.AccordionPanel(
            "Configure temp appearance and behavior with vast amount of settings or overwrite any part of "
            "component styles "
        ),
        dmc_table1
    ],
    value="flexibility1",
)

acc2=dmc.AccordionItem(
    [
        dmc.AccordionControl("Flexibility"),
        dmc.AccordionPanel(
            "Configure temp appearance and behavior with vast amount of settings or overwrite any part of "
            "component styles "
        ),
        dmc_table2
    ],
    value="flexibility2",
)

acc3=dmc.AccordionItem(
    [
        dmc.AccordionControl("Flexibility"),
        dmc.AccordionPanel(
            "Configure temp appearance and behavior with vast amount of settings or overwrite any part of "
            "component styles "
        ),
        dmc_table3,
    ],
    value="flexibility3",
)

acc4=dmc.AccordionItem(
    [
        dmc.AccordionControl("Flexibility"),
        dmc.AccordionPanel(
            "Configure temp appearance and behavior with vast amount of settings or overwrite any part of "
            "component styles "
        ),
        dmc_table,
    ],
    value="flexibility4",
)

app.layout = dmc.Accordion(
    children=[
        dmc.AccordionItem(
            [
                dmc.AccordionControl("LABOR IMPACT – SUMMARY"),
                dmc.AccordionPanel(
                    "LABOR IMPACT – SUMMARY"
                ),
            ],
            value="customization",
        ),
        dmc.Grid(
            children=[
                dmc.Col(acc0, span=6),
                # dmc.Col(acc1, span=2),
                # dmc.Col(acc2, span=2),
                # dmc.Col(acc3, span=2),
                dmc.Col(acc4, span=6),
            ],
            gutter="xs",
        )
    ],
)


if __name__ == "__main__":
    print(df)
    app.run_server()