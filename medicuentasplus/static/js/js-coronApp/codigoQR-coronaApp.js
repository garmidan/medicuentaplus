"use strict";
let informTest
var urlServicio = "https://apicovidqa.and.gov.co";
function cleanDate(e) {
    var t = e.split("T"),
        n = t[1].split(".");
    return t[0] + " " + n[0];
}
function cleanQR(e) {
    var t = e.split("|");
    return { ship: t[3], aerolinea: t[4], seat: t[5], travel_date: t[6] };
}
function makeDate(e) {
    return e.slice(0, 2) + "-" + e.slice(2, 4) + "-" + e.slice(4);
}
var sesion = localStorage.getItem("sesion");
if (null == sesion || "false" == sesion) location.href = "registro-coronApp.html";
else {

    

    var userdata = JSON.parse(localStorage.getItem("informacionusuario")),
        generateSet = {
            url: urlServicio + "/passport/api/v7.0/qr/generate",
            method: "POST",
            timeout: 0,
            headers: { "Content-Type": "application/problem+json; charset=utf-8", Authorization: "Bearer " + userdata.bearer_token },
            data: '{\r\n    "user_id": "' + userdata.user.id + '"\r\n}',
        };
        /// TestResult
        fetch(urlServicio + "/diagnosis/api/v1.0/TestResult", {
            method: 'GET', 
            headers:{
                'Content-Type': 'application/json',
                'Authorization': "Bearer " + userdata.bearer_token 
            }
            }).then(response => response.json())
            .then(data => {
                informTest = data;
                /// TestResult
                if (informTest.responseCode === "TEST_RESULT_TYPE1") {
                    $.ajax(generateSet).done(function (e) {
                        var t = e;
                        qrcode.stringToBytes = qrcode.stringToBytesFuncs["UTF-8"];
                        var n = qrcode(0, "L");
                        n.addData(decodeURIComponent(unescape(encodeURIComponent(t.qr))), "Byte"), n.make(), (document.getElementById("qrcode").innerHTML = n.createImgTag());
                        var a = cleanQR(t.qr);
                        var d = informTest.resultDate.split('T')[0];
                        document.getElementById("noviajar").style = "display:block;background-color: #b20624;padding: 5px;border-radius: 5px;text-align: center;color: white;";
                        document.getElementById("mensajeTest").innerHTML = 
                            "Su ultima fecha de toma de muestras en Sismuestras es del "+d+
                            ". Reclame su informe de resultado en el canal dispuesto por su EPS";
                        document.getElementById("noviajar").innerHTML = "NO DEBE VIAJAR <br> Debe Guardar Aislamiento";
                        (document.getElementById("saludo").innerHTML = "¡Hola <br/>" + userdata.user.firstname + "!"),
                            (document.getElementById("fechaVencimiento").innerHTML = cleanDate(t.expiration_date)),
                            (document.getElementById("nombre").innerHTML = userdata.user.firstname + " " + userdata.user.lastname),
                            (document.getElementById("tipoDoc").innerHTML = userdata.user.document_type.toUpperCase()),
                            (document.getElementById("numDocumento").innerHTML = userdata.user.document_number),
                            (document.getElementById("aerolinea").innerHTML = a.aerolinea),
                            (document.getElementById("numVuelo").innerHTML = a.ship),
                            (document.getElementById("silla").innerHTML = a.seat),
                            (document.getElementById("fechaVuelo").innerHTML = makeDate(a.travel_date)),
                            (document.getElementById("statusMovilidad").innerHTML = ''),
                            document.querySelector(".buttonsPopOvers").classList.add("QR" + "red"),
                            document.getElementById("cerrarSesion").addEventListener("click", function () {
                                localStorage.clear(), (location.href = "registro-coronApp.html");
                            }),
                            $("#btn-Convert-Html2Image").on("click", function () {
                                var e = $("#capturaQR")[0];
                                window.scrollTo(0, 0),
                                    html2canvas(e, {
                                        ignoreElements: function (e) {
                                            return "btn-Convert-Html2Image" === e.id;
                                        },
                                    }).then(function (e) {
                                        var t = e.toDataURL("image/jpg"),
                                            n =
                                                (t.replace(/^data:image\/jpg/, "data:application/octet-stream"),
                                                {
                                                    url: urlServicio + "/api/v1.0/email/sendemailwithattachment",
                                                    method: "POST",
                                                    timeout: 0,
                                                    headers: { "Content-Type": "application/problem+json; charset=utf-8", Authorization: "Bearer " + userdata.bearer_token },
                                                    data: '{\r\n    "attachment": "' + t + '"\r\n}',
                                                });
                                        $.ajax(n)
                                            .done(function (e) {
                                                $("#codigoQR").modal("show"), $("#btn-Convert-Html2Image").remove();
                                            })
                                            .fail(function (e) {
                                                console.log("fallo al envio de mail.");
                                            });
                                    });
                            });
                    });
                } else{
                    $.ajax(generateSet).done(function (e) {
                        var t = e;
                        qrcode.stringToBytes = qrcode.stringToBytesFuncs["UTF-8"];
                        var n = qrcode(0, "L");
                        n.addData(decodeURIComponent(unescape(encodeURIComponent(t.qr))), "Byte"), n.make(), (document.getElementById("qrcode").innerHTML = n.createImgTag());
                        var a = cleanQR(t.qr);
                        if (informTest.resultDate === null) {
                            document.getElementById("mensajeTest").innerHTML = 
                            "No hay registro de resultados de pruebas PCR o Antigeno en Sismuestras"
                        }else if(informTest.responseCode === "TEST_RESULT_TYPE2"){
                            var d = informTest.resultDate.split('T')[0];
                            document.getElementById("mensajeTest").innerHTML = 
                            "Su ultima fecha de toma de muestras en Sismuestras es del "+d+
                            ". Reclame su informe de resultado en el canal dispuesto por su EPS";
                        }
                        (document.getElementById("saludo").innerHTML = "¡Hola <br/>" + userdata.user.firstname + "!"),
                            (document.getElementById("fechaVencimiento").innerHTML = cleanDate(t.expiration_date)),
                            (document.getElementById("nombre").innerHTML = userdata.user.firstname + " " + userdata.user.lastname),
                            (document.getElementById("tipoDoc").innerHTML = userdata.user.document_type.toUpperCase()),
                            (document.getElementById("numDocumento").innerHTML = userdata.user.document_number),
                            (document.getElementById("aerolinea").innerHTML = a.aerolinea),
                            (document.getElementById("numVuelo").innerHTML = a.ship),
                            (document.getElementById("silla").innerHTML = a.seat),
                            (document.getElementById("fechaVuelo").innerHTML = makeDate(a.travel_date)),
                            (document.getElementById("statusMovilidad").innerHTML = t.qr_message),
                            console.log("");
                            if (t.qr_type == "yellow") {
                                document.querySelector(".buttonsPopOvers").classList.add("QR" + "green");
                            } else {
                                document.querySelector(".buttonsPopOvers").classList.add("QR" + t.qr_type);
                            }
                            document.getElementById("cerrarSesion").addEventListener("click", function () {
                                localStorage.clear(), (location.href = "registro-coronApp.html");
                            }),
                            $("#btn-Convert-Html2Image").on("click", function () {
                                var e = $("#capturaQR")[0];
                                window.scrollTo(0, 0),
                                    html2canvas(e, {
                                        ignoreElements: function (e) {
                                            return "btn-Convert-Html2Image" === e.id;
                                        },
                                    }).then(function (e) {
                                        var t = e.toDataURL("image/jpg"),
                                            n =
                                                (t.replace(/^data:image\/jpg/, "data:application/octet-stream"),
                                                {
                                                    url: urlServicio + "/api/v1.0/email/sendemailwithattachment",
                                                    method: "POST",
                                                    timeout: 0,
                                                    headers: { "Content-Type": "application/problem+json; charset=utf-8", Authorization: "Bearer " + userdata.bearer_token },
                                                    data: '{\r\n    "attachment": "' + t + '"\r\n}',
                                                });
                                        $.ajax(n)
                                            .done(function (e) {
                                                $("#codigoQR").modal("show"), $("#btn-Convert-Html2Image").remove();
                                            })
                                            .fail(function (e) {
                                                console.log("fallo al envio de mail.");
                                            });
                                    });
                            });
                    });
                }
            });
            
    
}
//# sourceMappingURL=codigoQR-coronaApp.js.map
