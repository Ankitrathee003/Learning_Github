import dash
from dash import html
import dash_ag_grid as dag
from dash.dependencies import Input, Output
import pandas as pd

# Sample DataFrame
df = pd.DataFrame({
    'Column 1': [1, 2, 3],
    'Column 2': [4, 5, 6],
    'Column 3': [None, None, None]  # Third column is initially blank
})

# Initialize Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Editable Grid with Dynamic Updates"),

    # AG Grid component
    dag.AgGrid(
        id="data-grid",
        columnDefs=[
            {"headerName": "Column 1", "field": "Column 1", "editable": False},
            {"headerName": "Column 2", "field": "Column 2", "editable": False},
            {"headerName": "Column 3", "field": "Column 3", "editable": True},  # Editable column
        ],
        rowData=df.to_dict("records"),
        defaultColDef={"resizable": True, "sortable": True},
        style={"height": "400px", "width": "600px"},
        # Enable event to capture cell edits
        eventListeners={
            "cellValueChanged": [
                """
                function(event) {
                    const gridApi = event.api;
                    const rowData = [];
                    gridApi.forEachNode(node => rowData.push(node.data));
                    event.source.api.setRowData(rowData);  // Update grid with modified data
                }
                """
            ]
        }
    ),

    # Output section to display the updated DataFrame
    html.Div(id="updated-df-output", style={"marginTop": "20px"}),
])


@app.callback(
    Output("updated-df-output", "children"),
    Input("data-grid", "rowData")
)
def update_dataframe(row_data):
    if row_data:
        # Create DataFrame from updated row data
        updated_df = pd.DataFrame(row_data)
        print("updaed datafrAMe is ",updated_df)
        return html.Pre(updated_df.to_string(index=False))
    return "No data available."


if __name__ == "__main__":
    app.run_server(debug=True)
