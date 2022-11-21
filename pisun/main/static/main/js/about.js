function l_image (a)
{
    image.src = a;
}


var theNum = "0";
let arr = ["1", "2", "3", "4"];
function change_img()
{
    if(theNum == arr.length)
{theNum="0";}
    image.src="{% static 'main/img/'"+arr[theNum]+"jpg' %}";

    theNum++;

}
