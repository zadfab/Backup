window.onload = init;
var save_id;
function init(){
    save_id = document.getElementById('add_customer_data');
    save_id.onclick = button_click;
    sched_id = document.getElementById('cust_refresh');
    sched_id.onclick = cust_refresh;

    }
function cust_refresh(){


}

function button_click(){
 var ezzy_id = document.getElementById('add_ezzy').value;
  var name = document.getElementById('add_name').value;
  var email = document.getElementById('add_email').value;
  var contact = document.getElementById('add_contact').value;
  var dnd = document.getElementById('add_dnd').value;


  var url = '/save_cust?name='+name+'&ezzy_id='+ezzy_id+'&email='+email+'&contact='+contact+'&dnd='+dnd;

    var req = new XMLHttpRequest();
      req.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
         alert(req.responseText);
        }
      };
      req.open("GET", url, true);
      req.send();
}
