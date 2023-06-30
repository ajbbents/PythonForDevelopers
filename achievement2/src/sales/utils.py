from books.models import Book
from io import BytesIO
import base64
import matplotlib.pyplot as plt


# define a function that takes the ID


def get_bookname_from_id(val):
    # this id is used to retrieve the name from the record
    bookname = Book.objects.get(id=val)
    # name is returned back
    return bookname


def get_graph():
    # create a BytesIO buffer for the image
    buffer = BytesIO()

    # create a plot with a BytesIO object as a file-like object. Set format to png
    plt.savefig(buffer, format='png')

    # set cursor to the beginning of the stream
    buffer.seek(0)

    # retrieve the content of the file
    image_png = buffer.getvalue()

    # encode the bytes-like object
    graph = base64.b64encode(image_png)

    # decode to get the string as output
    graph = graph.decode('utf-8')

    # free up the buffer memory
    buffer.close()

    # return the image/graph
    return graph

# chart_type: user input
# data: pandas dataframe


def get_chart(chart_type, data, **kwargs):
    # switch plot backend to Anti-Grain Geometry, write to file
    # AGG is preferred solution to write png files
    plt.switch_backend('AGG')

    # specify figure size
    fig = plt.figure(figsize=(6, 3))

    # select chart_type based on user input
    if chart_type == '#1':
        # plot bar between date on x and quantity on y
        plt.bar(data['date_created'], data['quantity'])

    elif chart_type == '#2':
        # generate pie based on price.
        # book titles sent from view as labels
        labels = kwargs.get('labels')
        plt.pie(data['price'], labels=labels)

    elif chart_type == '#3':
        # plot line based on date on x and price on y
        plt.plot(data['date_created'], data['price'])

    else:
        print('unknown chart type')

    # specify layout deets.
    plt.tight_layout()

    # render graph to file
    chart = get_graph()
    return chart
