/**
 * Created by w on 15-2-16.
 */
/*alert("python django中成功添加css js")*/
function views1(){
    var xmlhttp;
    if (window.XMLHttpRequest)
    { //ie7 firefox chrome opera safari
        xmlhttp=new XMLHttpRequest();
    }
    else{
        //ie6 ie5
        xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
    }
    xmlhttp.onreadystatechange=function()
    {
        if(xmlhttp.readyState==4 && xmlhttp.status)
        {
        // document.getElementById(usernametext).innerHTML='lonjioan'
            //username.innerHTML.indexOf('longjian');
           // alert(username)
            //document.write(usernametext)
           // username.write(longjian)
            er="<div id='er'>出错了</div>"
            document.write(er)

        }
    }
    xmlhttp.open('get','/ajax/',true);
    xmlhttp.send();
}