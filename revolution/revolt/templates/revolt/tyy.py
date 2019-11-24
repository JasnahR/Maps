{ % load
static %}
< !DOCTYPE
html >

< html >
< head >
< link
rel = "stylesheet"
href = "//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css" >
< link
rel = "stylesheet"
href = "//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css" >
< link
rel = "stylesheet"
type = "text/css"
href = "{% static 'revolt/main.css' %}" >
< title > < / title >

< meta
http - equiv = "content-type"
content = "text/html; charset=UTF-8" / >

< script
type = "text/javascript"
src = "https://gc.kis.v2.scr.kaspersky-labs.com/FD126C42-EBFA-4E12-B309-BB3FDD723AC1/main.js?attr=dZWB1wJGuN5efI6MAZyfpfhP502kVEy6C_kkw1JmlXWURWzOB6eU0bv4Ie_ACCTET96xZv9GRRVPCT3tWs6miEEUjwd3CBqs4z_BU3WMvXcCgZZhT_y3M0nL7S7y_cV7Noa6S4Y4I2U_0LOJWlvUb-G71Y9ev_RRnWuw_2XLq7MQ5k9puKyJnzWFpTU8xHbbRHcpRiValiJvsvH7Si-vMWd3jVmNfJ4ppCHuaGagJllO0iKaitTPkhi08z79mdL12pAvUyxAwsMeaL2kPXNq5Vg0jM3E2wgYKT2aDVKO7RfqpsAE7022wCEs0CAQzrRQFo_jThJTMlwFgnfXE8czqXDFAoXEp8uGSVS1OjBfY8kMLNp0g-1UewVWyUctXNutvWVavwe5KSDC61KAZArN8WU8fvXMoB2_vRyxh51dQa7TXeMgZN_XbH5ibuBYVzx6_aDgHpN-xghm2ByoArjZw7-zZ3WVPMhiFlVOiMv85_DznCeSrJqqFBPM3Oyk9jlYiWzW3S2xc1V-qkUDACji1vmm07T3wRHej1DxqnkJ3FDXvOt3qfaQsxRNAMRJx0s2bamVCahBd6ASgOQ8iqZUKl9TYNofRt5tKQtAzMs69tmFvYKHPw0JoEfQdma4RS54BKhez8TrvveKcKchDHQj6xvoowkPb1djoBpfh6Q9cXyL9Y9i8OwOoAKN2j3v8QhnJpzKv8Wdq4coAIcbqKUPOfVvcjQHAb-PU23IfU7PnHwLojiizUTz-iaetGJ8t5Rkk8LCBemxctVU4vGZORpdTqMdHOr181otsb0HMvpqRf89VBrOZbWiCuetPJoUHRmn8Kf2hApAXe3Olcou63zA_RPvF3UU8XGrFYze-5q-nyPf1yFwhy0Jm18fzMtxLMCtar8GfygFfeRiehQq68ROsPt5_2BPdNckQLo_LHZl1TypD5fPbSWQI-A_y-kr_wV9K1q2GKcQK0zhL9XyjCv7wm39TZecg8-i1Khr8h3oR9A1ig1s5CnHUgIWnU4SN-85xqpyMCmC3p1knRP3Bkf3FtFQvuzNP7RlYLMsn4RjiYjqBassu9BMbwFWUSeBteP0t3_w0lhENidFWJv8Nzme5hXf2Kc58QYJLQL2_91oclD-NOtjXl5siTE9XtJVAQgTojVXP3OZ8XJM2FetkdBnPvV1HcQP8-KVv5_5sjaW5WnEn7Ys96Ey_4VgVwwn74_wIgGOtPoDR3WGMKM2nBvp1A"
charset = "UTF-8" > < / script > < script >
L_NO_TOUCH = false;
L_DISABLE_3D = false;
< / script >

< script
src = "https://cdn.jsdelivr.net/npm/leaflet@1.5.1/dist/leaflet.js" > < / script >
< script
src = "https://code.jquery.com/jquery-1.12.4.min.js" > < / script >
< script
src = "https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js" > < / script >
< script
src = "https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.js" > < / script >
< link
rel = "stylesheet"
href = "https://cdn.jsdelivr.net/npm/leaflet@1.5.1/dist/leaflet.css" / >
< link
rel = "stylesheet"
href = "https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css" / >
< link
rel = "stylesheet"
href = "https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css" / >
< link
rel = "stylesheet"
href = "https://maxcdn.bootstrapcdn.com/font-awesome/4.6.3/css/font-awesome.min.css" / >
< link
rel = "stylesheet"
href = "https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.css" / >
< link
rel = "stylesheet"
href = "https://rawcdn.githack.com/python-visualization/folium/master/folium/templates/leaflet.awesome.rotate.css" / >
< style > html, body
{width: 100 %;
height: 100 %;
margin: 0;
padding: 0;} < / style >
< style >  # map {position:absolute;top:0;bottom:0;right:0;left:0;}</style>

< meta
name = "viewport"
content = "width=device-width,
initial - scale = 1.0, maximum - scale = 1.0, user - scalable = no
" />
< style >
# map_d43b6ee2d63c4a869353803e9686d66b {
position: relative;
width: 100.0 %;
height: 100.0 %;
left: 0.0 %;
top: 0.0 %;
}
< / style >

    < style >

    div.butt1
{
position: absolute;
top: 500
px;
left: 150
px;
width: 50
px;
height: 10
px;
}
div.t1
{
position: absolute;
top: 510
px;
left: 150
px;
width: 50
px;
height: 20
px;
}

div.butt2
{
position: absolute;
top: 500
px;
left: 200
px;
width: 50
px;
height: 10
px;
}
div.t2
{
position: absolute;
top: 510
px;
left: 200
px;
width: 50
px;
height: 20
px;
}

div.butt3
{
position: absolute;
top: 500
px;
left: 250
px;
width: 50
px;
height: 10
px;
}
div.t3
{
position: absolute;
top: 510
px;
left: 250
px;
width: 50
px;
height: 20
px;
}

div.butt4
{
position: absolute;
top: 500
px;
left: 250
px;
width: 50
px;
height: 10
px;
}
div.t4
{
position: absolute;
top: 510
px;
left: 250
px;
width: 50
px;
height: 20
px;
}

div.butt5
{
position: absolute;
top: 500
px;
left: 300
px;
width: 50
px;
height: 10
px;
}
div.t5
{
position: absolute;
top: 510
px;
left: 300
px;
width: 50
px;
height: 20
px;
}

div.butt6
{
position: absolute;
top: 500
px;
left: 350
px;
width: 50
px;
height: 10
px;
}
div.t6
{
position: absolute;
top: 510
px;
left: 350
px;
width: 50
px;
height: 20
px;
}

div.butt7
{
position: absolute;
top: 500
px;
left: 400
px;
width: 50
px;
height: 10
px;
}
div.t7
{
position: absolute;
top: 510
px;
left: 400
px;
width: 50
px;
height: 20
px;
}

div.butt8
{
position: absolute;
top: 500
px;
left: 450
px;
width: 50
px;
height: 10
px;
}
div.t8
{
position: absolute;
top: 510
px;
left: 450
px;
width: 50
px;
height: 20
px;
}

div.butt9
{
position: absolute;
top: 500
px;
left: 500
px;
width: 50
px;
height: 10
px;
}
div.t9
{
position: absolute;
top: 510
px;
left: 500
px;
width: 50
px;
height: 20
px;
}

div.butt10
{
position: absolute;
top: 500
px;
left: 550
px;
width: 50
px;
height: 10
px;
}
div.t10
{
position: absolute;
top: 510
px;
left: 550
px;
width: 50
px;
height: 20
px;
}

div.butt11
{
position: absolute;
top: 500
px;
left: 600
px;
width: 50
px;
height: 10
px;
}
div.t11
{
position: absolute;
top: 510
px;
left: 600
px;
width: 50
px;
height: 20
px;
}

div.butt12
{
position: absolute;
top: 500
px;
left: 650
px;
width: 50
px;
height: 10
px;
}
div.t12
{
position: absolute;
top: 510
px;
left: 650
px;
width: 50
px;
height: 20
px;
}

div.butt13
{
position: absolute;
top: 500
px;
left: 700
px;
width: 50
px;
height: 10
px;
}
div.t13
{
position: absolute;
top: 510
px;
left: 700
px;
width: 50
px;
height: 20
px;
}

div.butt14
{
position: absolute;
top: 500
px;
left: 750
px;
width: 50
px;
height: 10
px;
}
div.t14
{
position: absolute;
top: 510
px;
left: 750
px;
width: 50
px;
height: 20
px;
}

div.butt15
{
position: absolute;
top: 500
px;
left: 800
px;
width: 50
px;
height: 10
px;
}
div.t15
{
position: absolute;
top: 510
px;
left: 800
px;
width: 50
px;
height: 20
px;
}

div.butt2
{
position: absolute;
top: 500
px;
left: 200
px;
width: 50
px;
height: 10
px;
}
div.t2
{
position: absolute;
top: 510
px;
left: 200
px;
width: 50
px;
height: 20
px;
}

.bb
{
border: none;
width: 50
px;
height: 20
px;
}
h2
{
color: white;
font - size: 20
px;
}

h1
{
color:  # 04B4AE;
font - family: 'Lobster';
}

.page - header
{
background - color:  # 04B4AE;
margin - top: 0;
padding: 20
px
20
px
20
px
40
px;
}

.page - header
h1,.page - header
h1
a,.page - header
h1
a: visited, .page - header
h1
a: active
{
color:  # ffffff;
font - size: 36
pt;
text - decoration: none;
}

}

< / style >

    < / head >
        < body >

        < div


class ="page-header" >

< h1 > < a
href = "/" > Industrial
revolution < / a > < / h1 >
< / div >
< div


class ="butt1" >

< button


class ="bb" onmouseover="map1()" onmouseout="o1()" onclick="map1()" width="10" > < / button >

< / div >
< div


class ="t1" >

< h2
id = "1"
color = "white" > 1700 < / h2 >
< / div >

< div


class ="butt2" >

< button


class ="bb" onmouseover="i2()" onmouseout="o2()" width="10" > < / button >

< / div >
< div


class ="t2" >

< h2
id = "2"
color = "white" > 1710 < / h2 >
< / div >

< div


class ="butt3" >

< button


class ="bb" onmouseover="i3()" onmouseout="o3()" width="10" > < / button >

< / div >
< div


class ="t3" >

< h2
id = "3"
color = "white" > 1720 < / h2 >
< / div >

< div


class ="butt4" >

< button


class ="bb" onmouseover="i4()" onmouseout="o4()" width="10" > < / button >

< / div >
< div


class ="t4" >

< h2
id = "4"
color = "white" > 1730 < / h2 >
< / div >

< div


class ="butt5" >

< button


class ="bb" onmouseover="i5()" onmouseout="o5()" width="10" > < / button >

< / div >
< div


class ="t5" >

< h2
id = "5"
color = "white" > 1740 < / h2 >
< / div >

< div


class ="butt6" >

< button


class ="bb" onmouseover="i6()" onmouseout="o6()" width="10" > < / button >

< / div >
< div


class ="t6" >

< h2
id = "6"
color = "white" > 1750 < / h2 >
< / div >

< div


class ="butt7" >

< button


class ="bb" onmouseover="i7()" onmouseout="o7()" width="10" > < / button >

< / div >
< div


class ="t7" >

< h2
id = "7"
color = "white" > 1760 < / h2 >
< / div >

< div


class ="butt8" >

< button


class ="bb" onmouseover="i8()" onmouseout="o8()" width="10" > < / button >

< / div >
< div


class ="t8" >

< h2
id = "8"
color = "white" > 1770 < / h2 >
< / div >

< div


class ="butt9" >

< button


class ="bb" onmouseover="i9()" onmouseout="o9()" width="10" > < / button >

< / div >
< div


class ="t9" >

< h2
id = "9"
color = "white" > 1780 < / h2 >
< / div >

< div


class ="butt10" >

< button


class ="bb" onmouseover="i10()" onmouseout="o10()" width="10" > < / button >

< / div >
< div


class ="t10" >

< h2
id = "10"
color = "white" > 1790 < / h2 >
< / div >

< div


class ="butt11" >

< button


class ="bb" onmouseover="i11()" onmouseout="o11()" width="10" > < / button >

< / div >
< div


class ="t11" >

< h2
id = "11"
color = "white" > 1800 < / h2 >
< / div >

< div


class ="butt12" >

< button


class ="bb" onmouseover="i12()" onmouseout="o12()" width="10" > < / button >

< / div >
< div


class ="t12" >

< h2
id = "12"
color = "white" > 1810 < / h2 >
< / div >

< div


class ="butt13" >

< button


class ="bb" onmouseover="i13()" onmouseout="o13()" width="10" > < / button >

< / div >
< div


class ="t13" >

< h2
id = "13"
color = "white" > 1820 < / h2 >
< / div >

< div


class ="butt14" >

< button


class ="bb" onmouseover="i14()" onmouseout="o14()" width="10" > < / button >

< / div >
< div


class ="t14" >

< h2
id = "14"
color = "white" > 1830 < / h2 >
< / div >

< div


class ="butt15" >

< button


class ="bb" onmouseover="i15()" onmouseout="o15()" width="10" > < / button >

< / div >
< div


class ="t15" >

< h2
id = "15"
color = "white" > 1840 < / h2 >
< / div >
< script >
function
i1()
{
    document.getElementById("1").style.color = "#04B4AE";
}
function
o1()
{
    document.getElementById("1").style.color = "white";
}

function
i2()
{
    document.getElementById("2").style.color = "#04B4AE";
}
function
o2()
{
    document.getElementById("2").style.color = "white";
}

function
i3()
{
    document.getElementById("3").style.color = "#04B4AE";
}
function
o3()
{
    document.getElementById("3").style.color = "white";
}

function
i4()
{
    document.getElementById("4").style.color = "#04B4AE";
}
function
o4()
{
    document.getElementById("4").style.color = "white";
}

function
i5()
{
    document.getElementById("5").style.color = "#04B4AE";
}
function
o5()
{
    document.getElementById("5").style.color = "white";
}

function
i6()
{
    document.getElementById("6").style.color = "#04B4AE";
}
function
o6()
{
    document.getElementById("6").style.color = "white";
}

function
i7()
{
    document.getElementById("7").style.color = "#04B4AE";
}
function
o7()
{
    document.getElementById("7").style.color = "white";
}

function
i8()
{
    document.getElementById("8").style.color = "#04B4AE";
}
function
o8()
{
    document.getElementById("8").style.color = "white";
}

function
i9()
{
    document.getElementById("9").style.color = "#04B4AE";
}
function
o9()
{
    document.getElementById("9").style.color = "white";
}

function
i10()
{
    document.getElementById("10").style.color = "#04B4AE";
}
function
o10()
{
    document.getElementById("10").style.color = "white";
}

function
i11()
{
    document.getElementById("11").style.color = "#04B4AE";
}
function
o11()
{
    document.getElementById("11").style.color = "white";
}

function
i12()
{
    document.getElementById("12").style.color = "#04B4AE";
}
function
o12()
{
    document.getElementById("12").style.color = "white";
}

function
i13()
{
    document.getElementById("13").style.color = "#04B4AE";
}
function
o13()
{
    document.getElementById("13").style.color = "white";
}

function
i14()
{
    document.getElementById("14").style.color = "#04B4AE";
}
function
o14()
{
    document.getElementById("14").style.color = "white";
}

function
i15()
{
    document.getElementById("15").style.color = "#04B4AE";
}
function
o15()
{
    document.getElementById("15").style.color = "white";
}

< / script >
< / body >
