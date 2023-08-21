import dash_mantine_components as dmc
from dash import Dash, Output, Input, html, callback

app = Dash(__name__)

app.layout = html.Div(
    [
        dmc.Select(
            label="Select framework",
            placeholder="Select one",
            id="framework-select",
            value="ng",
            data=[
                {"value": "react", "label": "React"},
                {"value": "ng", "label": "Angular"},
                {"value": "svelte", "label": "Svelte"},
                {"value": "vue", "label": "Vue"},
            ],
            style={"width": 200, "marginBottom": 10},
        ),
        dmc.Text(id="selected-value"),
    ]
)


@callback(Output("selected-value", "children"), Input("framework-select", "value"))
def select_value(value):
    return value

if __name__ == "__main__":
    app.run_server(debug=True)