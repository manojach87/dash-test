import dash_mantine_components as dmc
from dash import Dash, Output, Input, html, callback, State

app = Dash(__name__)


dmc_modal = dmc.Modal(
            title="New Modal",
            id="modal-simple",
            zIndex=10000,
            children=[
                dmc.Text("Select Group."),
                dmc.Space(h=20),
                dmc.Group(
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
                        dmc.Button("Submit", id="modal-submit-button"),
                        dmc.Button(
                            "Close",
                            color="red",
                            variant="outline",
                            id="modal-close-button",
                        ),
                    ],
                    position="right",
                ),
            ],
        )

app.layout = html.Div(
    [
        dmc.Text(id="selected-value"),
        dmc.Button("Open Modal", id="modal-demo-button"),
        dmc_modal

    ]
)

@callback(
    Output("modal-simple", "opened"),
    Input("modal-demo-button", "n_clicks"),
    Input("modal-close-button", "n_clicks"),
    Input("modal-submit-button", "n_clicks"),
    State("modal-simple", "opened"),
    prevent_initial_call=True,
)
def modal_demo(nc1, nc2, nc3, opened):
    return not opened

@callback(Output("selected-value", "children"), Input("framework-select", "value"))
def select_value(value):
    return value

if __name__ == "__main__":
    app.run_server(debug=True)