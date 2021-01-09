from django.shortcuts import render
from django.http import HttpResponse
from .models import template_table,scheduler_table,message_forwarding_log,customer_table
# Create your views here.
def homepage(request):
    customer_data = customer_table.objects.all()
    schedule = scheduler_table.objects.all()
    template = template_table.objects.all()
    message = message_forwarding_log.objects.all()
    print("schedule id _auto",schedule.get(id=1))
    print("schedule id _auto",schedule.get(id=2))
    print("schedule id _auto",schedule.get(id=3))
    print("schedule id _auto",schedule.get(id=4))

    import plotly
    import plotly.offline as pyo
    import plotly.graph_objects as go
    x_list = ["sep/1/2020","sep/2/2020","sep/3/2020","sep/4/2020","sep/5/2020","sep/6/2020"]
    y_list = [2,6,7,0,20,10]




    fig = go.Figure()
    fig.add_trace(go.Bar(x = x_list, y = y_list))
    fig.update_layout(height=700, hovermode = 'x', xaxis_tickangle=45,title_text = "Message Read Graph",yaxis=dict(
        title='Message read',
        titlefont_size=16,

        tickfont_size=14,
    ),
    xaxis=dict(
            title='Date',
            titlefont_size=16,
            tickfont_size=14,
    ),)
    plotly.io.write_html(fig,full_html=False,file = "static/optimised_graph.html",config={"displayModeBar": False, "showTips": False})
    animals= ["sep/1/2020","sep/2/2020","sep/3/2020","sep/4/2020","sep/5/2020","sep/6/2020"]

    fig = go.Figure(data=[
        go.Bar(name='Message Send Successfully ', x=animals, y=[20, 14, 23,21,8,6]),
        go.Bar(name='message Failed', x=animals, y=[12, 18, 29,9,3,1])
    ])
    # Change the bar mode
    fig.update_layout(barmode='stack',height=700,xaxis_tickangle=45)


    param = {"customer_data":customer_data,"schedule_data":schedule,"template_data":template,"message_data":message,"graph":fig}
    return render(request,"design/index_django.html",param)


"""
def graph(request):
    import plotly
    import plotly.offline as pyo
    import plotly.graph_objects as go
    x_list = ["sep/1/2020","sep/2/2020","sep/3/2020","sep/4/2020","sep/5/2020","sep/6/2020"]
    y_list = [2,6,7,0,20,10]



    data = [go.Bar(x = x_list,y = y_list , name = "demo chart",)]


    layout = go.Layout(title = "   Message read per day" ,xaxis_title="Date",yaxis_title="Message read")

    figure = go.Figure(data= data,layout=layout)
    plotly.io.write_html(figure,full_html=False,file = "static/optimised_graph.html",config={"displayModeBar": False, "showTips": False})
    return render(request,"graph.html")

"""
"""
def grp_rndr(request):
    return render(request,"optimised_graph.html")
"""
def update(request):
    if request.method == "POST":
        name = request.POST["name"]
        ezzy_id = request.POST["ezzy_id"]
        email = request.POST["email"]
        contact= request.POST["contact"]
        dnd= request.POST["dnd"]
        print(name,ezzy_id,contact,email,dnd)
    customer_data = customer_table.objects.all()
    schedule = scheduler_table.objects.all()
    template = template_table.objects.all()
    message = message_forwarding_log.objects.all()
    try:
        to_add = (customer_data.order_by("id").last().id)
    except:
        to_add=0
    ezzy_id_add = "ezzy_"+str(to_add+1).zfill(6)
    print(ezzy_id_add)
    sv = customer_table(ezzy_id=ezzy_id_add,customer_name=name,email_address=email,phone_number=contact,DND_status=dnd)
    sv.save()

    param = {"customer_data":customer_data,"schedule_data":schedule,"template_data":template,"message_data":message}
    return render(request,"design/index_django.html",param)

def ajax_update(request):
    ezzy = request.GET.get('ezzy_id')
    name = request.GET.get('name')
    email = request.GET.get('email')
    contact = request.GET.get('contact')
    dnd = request.GET.get('dnd')
    print(ezzy,name,email,contact,dnd)
    try:
        sv = customer_table(ezzy_id=ezzy,customer_name=name,email_address=email,phone_number=contact,DND_status=dnd)
        sv.save()
        param = {"1":"hello","2":"zad"}
        return HttpResponse(param)
    except:
        return HttpResponse("Error occur")

def jquery_ajax(request):
    if request.method == "POST":
        name = request.POST['name']
        password = request.POST['password']
    return HttpResponse("Done")
def open(request):
    return render(request,"jquery_ajax.html")