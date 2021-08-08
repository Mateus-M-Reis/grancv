# AUTOGENERATED! DO NOT EDIT! File to edit: 01_outputs.ipynb (unless otherwise specified).

__all__ = ['PandasTable', 'markdown', 'info_snackbar', 'dialog_button', 'container', 'row', 'column']

# Cell
import ipyvuetify
#from nbdev.imports import *

# Cell

import pandas as pd
import traitlets
import json

class PandasTable(ipyvuetify.VuetifyTemplate):
    """
    Vuetify DataTable rendering of a pandas DataFrame

    Args:
        data (pandas.DataFrame) - the data to render
        title (str) - optional title

    Modified from Source: https://jupyter-tutorial.readthedocs.io/de/latest/workspace/jupyter/ipywidgets/libs/ipyvuetify.html
    """

    headers = traitlets.List([]).tag(sync=True, allow_null=True)
    items = traitlets.List([]).tag(sync=True, allow_null=True)
    search = traitlets.Unicode('').tag(sync=True)
    title = traitlets.Unicode('DataFrame').tag(sync=True)
    index_col = traitlets.Unicode('').tag(sync=True)
    template = traitlets.Unicode('''
        <template>
          <v-card>
            <v-card-title>
              <span class="title font-weight-bold">{{ title }}</span>
              <v-spacer></v-spacer>
                <v-text-field
                    v-model="search"
                    append-icon="search"
                    label="Search ..."
                    single-line
                    hide-details
                ></v-text-field>
            </v-card-title>
            <v-data-table
                :headers="headers"
                :items="items"
                :search="search"
                :item-key="index_col"
                :rows-per-page-items="[25, 50, 250, 500]"
            >
                <template v-slot:no-data>
                  <v-alert :value="true" color="error" icon="warning">
                    Sorry, nothing to display here :(
                  </v-alert>
                </template>
                <template v-slot:no-results>
                    <v-alert :value="true" color="warning" icon="warning">
                      Your search for "{{ search }}" found no results.
                    </v-alert>
                </template>
                <template v-slot:items="rows">
                  <td v-for="(element, label, index) in rows.item"
                      @click=cell_click(element)
                      >
                    {{ element }}
                  </td>
                </template>
            </v-data-table>
          </v-card>
        </template>
        ''').tag(sync=True)

    def __init__(self, *args,
                 data=pd.DataFrame(),
                 title=None,
                 **kwargs):
        super().__init__(*args, **kwargs)
        data = data.reset_index()
        self.index_col = data.columns[0]
        headers = [{
              "text": col,
              "value": col
            } for col in data.columns]
        headers[0].update({'align': 'left', 'sortable': True})
        self.headers = headers
        self.items = json.loads(
            data.to_json(orient='records'))
        if title is not None:
            self.title = title


# Cell

from markdown import markdown as md
import ipywidgets
def markdown(*args, **kwargs):
    """
    Render input string(s) as markdown

    Parameters
    *args : str or list of strings
        String(s) to render as markdown
    **kwargs : any
        arguments supported by the markdown class

    """
    return ipywidgets.HTML(
        md(
            '\n'.join(args),
            **kwargs
        )
    )

# Cell

class _InfoSnackbar(ipyvuetify.VuetifyTemplate):
    color = traitlets.Unicode("primary").tag(sync=True, allow_null=True)
    message = traitlets.Unicode("").tag(sync=True, allow_null=False)
    timeout = traitlets.Integer(5000).tag(sync=True, allow_null=True)
    active = traitlets.Bool(True).tag(sync=True, allow_null=True)
    multi_line = traitlets.Bool(True).tag(sync=True, allow_null=True)

    template = traitlets.Unicode(
        """
        <template>
            <v-snackbar
                v-model="active"
                centered=true
                :color="color"
                elevation=0
                :multi-line="multi_line"
                :timeout="timeout"
            >
              {{message}}

            <v-btn
              color="white"
              text
              @click="active = false"
            >
              Close
            </v-btn>

            </v-snackbar>
          </template>

        """
    ).tag(sync=True)

    def __init__(
        self,
        snackbar=False,
        message=None,
        multi_line=True,
        color="primary",
        timeout=6000,
        active=True,
        *args,
        **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.color = color
        self.timeout = timeout
        self.active = active
        self.message = message
        self.multi_line = multi_line

def info_snackbar(snackbar=False,
        message=None,
        multi_line=True,
        color="primary",
        timeout=6000,
        active=True):
    """
    snackbar widget

    Useful for displaying information/messages

    message : str
        Status message to display
    timeout : int, optional default 6000
        How long to display the message (in milliseconds)
    multi_line : bool, optional default True
        Whether the snackbar should be multi-line (or not)
    color : str, optional default 'primary'
        ipyvuetify color of snackbar
        Typical options include ['primary','error','warning','success']
    active : bool, optional, default True
        Whether to display snackbar
        """
    return _InfoSnackbar(snackbar=snackbar,
                        message=message,
                        multi_line=multi_line,
                        color=color,
                        timeout=timeout,
                        active=active)

# Cell


def dialog_button(label='',
                  icon='mdi-help',
                  _class="icon ma-2",
                  _style="",
                  color="primary",
                  dark=False,
                  dialog_width=600,
                  dialog_title="Dialog Title",
                  dialog_content="Dialog Content",
                ):
    """
    Creates a button and activates a dialog on click

    Useful to display application documentation/help

    Parameters
    ----------
    icon : str (optional, default None)
        Icon to display on button
    label : str (optoinal, default None)
        Text to display on button
    dialog_width : int (optional, default 600)
        Width of the dialog in pixels
    dialog_title : str (optional, default 'Help Title')
        Dialog title
    dialog_content : str (optional, default '')
        Dialog content in markdown format
    color : str (optional, default 'primary')
        Color of button
    dark : bool
        Use dark style
    _class : str (optional, default 'icon ma-2')
        CSS classes of button
    _style: str
        CSS style of button
    """

    if icon is None:
        icon=''

    if label is None:
        label=''

    dialog_button = ipyvuetify.Btn(
        _class_="icon ma-2",
        _style='',
        color=color,
        depressed=True,
        dark=dark,
        children=[label, ipyvuetify.Icon(children=[icon])],
    )

    close_dialog_btn = ipyvuetify.Btn(children=["Close"])

    dialog_dialog = ipyvuetify.Dialog(
        v_model=False,
        scrollable=True,
        width=dialog_width,
        children=[
            ipyvuetify.Card(children=[
                ipyvuetify.CardTitle(class_="headline pa-4",
                                     children=[dialog_title]),
                ipyvuetify.Divider(),
                ipyvuetify.CardText(
                    class_="pa-4 text--primary",
                    primary_title=True,
                    children=[dialog_content],
                ),
                ipyvuetify.Divider(),
                close_dialog_btn,
            ])
        ],
    )

    def open_dialog_dialog(widget, event, data):
        dialog_dialog.v_model = True

    def close_dialog_dialog(widget, event, data):
        dialog_dialog.v_model = False

    display(ipyvuetify.Layout(children=[dialog_dialog]))
    close_dialog_btn.on_event("click", close_dialog_dialog)
    dialog_button.on_event("click", open_dialog_dialog)
    return dialog_button

# Cell


def container(
    children=[],
    fluid=False,
    class_="icon ma-2",
    style_="",
):
    """
    Creates a button and activates a dialog on click

    Useful to display application documentation/help

    Parameters
    ----------
    children : list
        List of elements to display in container
    fluid : bool (default False)
        Removes viewport maximum-width size breakpoints
    _class : str (optional, default 'icon ma-2')
        CSS classes of button
    _style: str
        CSS style of button
    """

    ret = ipyvuetify.Container(
        class_=class_,
        style_=style_,
        children=children,
        fluid=fluid,
    )

    return ret

# Cell


def row(
    children=[],
    align=None,
    align_content=None,
    justify=None,
    dense=False,
    no_gutters=False,
    class_="",
    style_="",
):
    """
    Create a row output container

    For details see: https://vuetifyjs.com/en/components/grids/

    Parameters
    ----------
    children : list (default [])
        List of elements to display in container
    align : str (default None)
        Applies the align-items css property. Available options are start, center, end, baseline and stretch.
    align_content : str (default None)
        Applies the align-content css property. Available options are start, center, end, space-between, space-around and stretch.
    justify : str (default None)
        Applies the justify-content css property. Available options are start, center, end, space-between and space-around.
    dense : bool (default False)
        Reduces the gutter between v-cols.
    no_gutters : bool (default False)
        Removes the gutter between v-cols.
    _class : str (optional, default 'icon ma-2')
        CSS classes of button
    _style: str
        CSS style of button
    """

    ret = ipyvuetify.Row(
        children=children,
        align=align,
        align_content=align_content,
        justify=justify,
        dense=dense,
        no_gutters=no_gutters,
        class_=class_,
        style_=style_,
    )

    return ret

# Cell


def column(
    children=[],
    cols=None,
    offset=None,
    order=None,
    align_self=None,
    class_="",
    style_="",
):
    """
    Create a column output container

    For details see: https://vuetifyjs.com/en/components/grids/

    Parameters
    ----------
    children : list (default [])
        List of elements to display in container
    cols : None, str, int
        Sets the default number of columns the component extends. Available options are 1 -> 12 and auto.
    offset : None, str, int
        Sets the default offset for the column.
    order: None
        Sets the default order for the column.
    align_self : None, str, int
        Applies the align-items css property. Available options are start, center, end, auto, baseline and stretch. See https://developer.mozilla.org/en-US/docs/Web/CSS/align-items
    class_ : str (optional, default 'icon ma-2')
        CSS classes of button
    style_: str
        CSS style of button
    """

    ret = ipyvuetify.Col(
        children=children,
        cols=cols,
        offset=offset,
        order=order,
        align_self=align_self,
        class_=class_,
        style_=style_,
        justify_space_between=True,
    )

    return ret
