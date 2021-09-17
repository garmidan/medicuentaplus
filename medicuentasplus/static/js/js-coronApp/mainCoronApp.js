"use strict";
let informTest;
var sesion = localStorage.getItem("sesion"),
    urlServicio = "https://apicovidqa.and.gov.co";
function logout() {
    localStorage.clear(), (location.href = "registro-coronApp.html");
}
if (null == sesion || "false" == sesion) 
    location.href = "registro-coronApp.html";
else {
    document.getElementById("cerrarSesion").addEventListener("click", logout);
    var informuser = localStorage.getItem("informacionusuario");
    
    if (informuser) {

        

      
        var total = function (e) {
                if (e.valid_qr) {
                    var a = {
                        url: urlServicio + "/passport/api/v7.0/qr/generate",
                        method: "POST",
                        timeout: 0,
                        headers: { "Content-Type": "application/problem+json; charset=utf-8", Authorization: "Bearer " + datos.bearer_token },
                        data: '{\r\n    "user_id": "' + datos.user.id + '"\r\n}',
                    };
                    $.ajax(a).done(function (e) {
                        localStorage.setItem("codigoQR", JSON.stringify(e)), (location.href = "codigoQR-coronApp.html");
                    });
                } else
                    $(document).ready(function () {
                        document.getElementById("datosuser").innerHTML = "¡Hola <br/>" + datos.user.firstname + "!";
                        var e = {
                                url: urlServicio + "/api/v2.0/authentication/refresh-token",
                                method: "POST",
                                timeout: 0,
                                headers: { "Content-Type": "application/problem+json; charset=utf-8" },
                                data: '{\r\n    "refresh_token": "' + datos.refresh_token + '"}',
                            },
                            a = $.ajax(e),
                            t = { url: urlServicio + "/diagnosis/api/v1.0/travel/airlines", method: "GET", timeout: 0, headers: { "Content-Type": "application/problem+json; charset=utf-8" } },
                            d = "";
                        a.done(function () {
                            var e = $.ajax(t);
                            d = e.done(function () {
                                !(function () {
                                    var e = {
                                            url: urlServicio + "/diagnosis/api/v2.0/form/full",
                                            method: "GET",
                                            timeout: 0,
                                            mode: "no-cors",
                                            credentials: "include",
                                            headers: { "Content-Type": "application/problem+json; charset=utf-8", "Access-Control-Allow-Origin": "*", Authorization: "Bearer " + a.responseJSON.bearer_token },
                                        },
                                        t = $.ajax(e);
                                    function i() {
                                        var e,
                                            i,
                                            o = 0,
                                            n = [],
                                            r = [],
                                            c = [],
                                            s = [],
                                            f = [],
                                            u = [],
                                            l = [],
                                            b = [],
                                            h = datos.user.id,
                                            p = new Date();
                                        if (1 == String(p.getDate()).length) var g = "0" + String(p.getDate());
                                        else g = p.getDate();
                                        if (1 == String(p.getMonth() + 1).length) var m = "0" + String(p.getMonth() + 1);
                                        else m = String(p.getMonth() + 1);
                                        if (1 == String(p.getHours()).length) var v = "0" + String(p.getHours());
                                        else v = String(p.getHours());
                                        if (1 == String(p.getMinutes()).length) var S = "0" + String(p.getMinutes());
                                        else S = String(p.getMinutes());
                                        if (1 == String(p.getSeconds()).length) var E = "0" + String(p.getSeconds());
                                        else E = String(p.getSeconds());
                                        var _ = [g, m, p.getFullYear()].join("/") + " " + [v, S, E].join(":");
                                        p = _;
                                        var y = a.responseJSON.bearer_token,
                                            j = t.responseJSON.preguntas,
                                            O = (t.responseJSON.diagnosticos, 0),
                                            k = "abf94fbd-e3c6-4dca-aa65-9b735b67e8a9",
                                            w = "8304df35-1948-4445-89a0-e2d482447c7e",
                                            N = "e1154e34-0d63-4741-a106-cd0c3113053d",
                                            T = "f4ca08c5-cdd9-4cb2-8a71-634e0a39b3aa",
                                            I = "121ea483-6495-4a5d-94b1-84bea278a70b",
                                            J = "09ba9d8e-ce70-4445-87d4-650a373a0a56";
                                        new Vue({
                                            el: "#app",
                                            data: { preguntas: t.responseJSON.preguntas, diagnosticos: t.responseJSON.diagnosticos, aerolineas: d.responseJSON.data },
                                            methods: {
                                                mostrarpreguntas: function () {
                                                    j.forEach(function (e) {
                                                        1 == ++o && ($("#c9a60560-97b2-47da-9e70-30ca29b98add").show(), $("#empezar").hide());
                                                    });
                                                },
                                                seleccionadas: function (a, t) {
                                                    if (((O = 0), "c9a60560-97b2-47da-9e70-30ca29b98add" === a))
                                                        j.filter(function (e) {
                                                            return "c9a60560-97b2-47da-9e70-30ca29b98add" === e.id;
                                                        }).forEach(function (e) {
                                                            e.respuestas.forEach(function (e) {
                                                                1 == $("#" + e.id).is(":checked") && n.push(e.id);
                                                            });
                                                            var a = { id: "c9a60560-97b2-47da-9e70-30ca29b98add", respuestas: n };
                                                            $("#cdbc8c94-a47d-4f05-9bb6-b3cde9dd8fcd").show(), $("#c9a60560-97b2-47da-9e70-30ca29b98add").hide(), $("#" + t).hide(), b.push(a);
                                                        });
                                                    else if ("cdbc8c94-a47d-4f05-9bb6-b3cde9dd8fcd" === a) {
                                                        j.filter(function (e) {
                                                            return "cdbc8c94-a47d-4f05-9bb6-b3cde9dd8fcd" === e.id;
                                                        }).forEach(function (e) {
                                                            e.respuestas.forEach(function (e) {
                                                                1 == $("#" + e.id).is(":checked") && r.push(e.id);
                                                            });
                                                        });
                                                        var d = { id: "cdbc8c94-a47d-4f05-9bb6-b3cde9dd8fcd", respuestas: r };
                                                        $("#cdbc8c94-a47d-4f05-9bb6-b3cde9dd8fcd").hide(), b.push(d);
                                                        var o = !1,
                                                            g = !1;
                                                        n.includes("a3e3d8ef-98e4-4287-80cd-a1633817fe08") || n.includes("f5400ee7-eaf5-4520-b4f5-2f53754f0c38") || (n.length >= 3 && !n.includes("abf94fbd-e3c6-4dca-aa65-9b735b67e8a9"))
                                                            ? (g = !0)
                                                            : 2 != n.length || n.includes("abf94fbd-e3c6-4dca-aa65-9b735b67e8a9")
                                                            ? r.length >= 1 && !r.includes("8304df35-1948-4445-89a0-e2d482447c7e")
                                                                ? (o = !0)
                                                                : (r.includes("8304df35-1948-4445-89a0-e2d482447c7e") || n.length <= 1) &&
                                                                  (e = { fecha: p, diagnostico: (i = "cb388ab6-9bf3-4033-ab06-da16d5c2d819"), id_usuario: h, preguntas: b })
                                                            : (o = !0),
                                                            g ? $("#3aa6a7d3-53ce-4860-af22-718f83f5b8fc").show() : o && $("#5a1dd7ae-b099-4381-a7c8-d3d82abbb6d1").show();
                                                    } else if ("5a1dd7ae-b099-4381-a7c8-d3d82abbb6d1" === a) {
                                                        j.filter(function (e) {
                                                            return "5a1dd7ae-b099-4381-a7c8-d3d82abbb6d1" === e.id;
                                                        }).forEach(function (e) {
                                                            e.respuestas.forEach(function (e) {
                                                                1 == $("#" + e.id).is(":checked") && c.push(e.id);
                                                            });
                                                        });
                                                        var m = { id: "5a1dd7ae-b099-4381-a7c8-d3d82abbb6d1", respuestas: c };
                                                        $("#5a1dd7ae-b099-4381-a7c8-d3d82abbb6d1").hide(),
                                                            b.push(m),
                                                            (e = r.includes("1e162809-e09b-4a6d-bcdf-615668a5e5f3")
                                                                ? { fecha: p, diagnostico: (i = "3abd2ea9-74e3-4945-aac7-454498198203"), id_usuario: h, preguntas: b }
                                                                : { fecha: p, diagnostico: (i = "e66ded72-c55a-4ec2-8d88-df2e6db844cb"), id_usuario: h, preguntas: b });
                                                    } else if ("3aa6a7d3-53ce-4860-af22-718f83f5b8fc" === a) {
                                                        j.filter(function (e) {
                                                            return "3aa6a7d3-53ce-4860-af22-718f83f5b8fc" === e.id;
                                                        }).forEach(function (e) {
                                                            e.respuestas.forEach(function (e) {
                                                                1 == $("#" + e.id).is(":checked") && s.push(e.id);
                                                            });
                                                            var a = { id: "3aa6a7d3-53ce-4860-af22-718f83f5b8fc", respuestas: s };
                                                            $("#c56d6fc8-0ab0-4ade-89e3-bbb58b3d025a").show(), $("#3aa6a7d3-53ce-4860-af22-718f83f5b8fc").hide(), $("#" + t).hide(), b.push(a);
                                                        });
                                                    } else if ("c56d6fc8-0ab0-4ade-89e3-bbb58b3d025a" === a) {
                                                        j
                                                            .filter(function (e) {
                                                                return "c56d6fc8-0ab0-4ade-89e3-bbb58b3d025a" === e.id;
                                                            })
                                                            .forEach(function (e) {
                                                                e.respuestas.forEach(function (e) {
                                                                    1 == $("#" + e.id).is(":checked") && f.push(e.id);
                                                                });
                                                                var a = { id: "c56d6fc8-0ab0-4ade-89e3-bbb58b3d025a", respuestas: f };
                                                                $("#c56d6fc8-0ab0-4ade-89e3-bbb58b3d025a").hide(), $("#" + t).hide(), b.push(a);
                                                            }),
                                                            f.includes("3509e425-75dd-4e52-9f6b-31d9a1c1ca84") && !s.includes("7129174f-ec7d-4449-b4a5-8e965f99787a") && 1 == s.length
                                                                ? (e = { fecha: p, diagnostico: (i = "74c80274-9b1b-493f-9c69-653ab72d0dd9"), id_usuario: h, preguntas: b })
                                                                : (s.length >= 1 && s.includes("7129174f-ec7d-4449-b4a5-8e965f99787a")) || (f.includes("ebec7eec-cfec-4ddd-9677-5847cb3fc690") && s.length >= 1)
                                                                ? $("#b478c479-e0e4-4f5c-93a8-da5e3afc15f3").show()
                                                                : (e = { fecha: p, diagnostico: (i = "bb01f096-0ced-4672-b50f-7e30c4a06d54"), id_usuario: h, preguntas: b });
                                                    } else if ("b478c479-e0e4-4f5c-93a8-da5e3afc15f3" === a) {
                                                        j.filter(function (e) {
                                                            return "b478c479-e0e4-4f5c-93a8-da5e3afc15f3" === e.id;
                                                        }).forEach(function (e) {
                                                            e.respuestas.forEach(function (e) {
                                                                1 == $("#" + e.id).is(":checked") && u.push(e.id);
                                                            });
                                                            var a = { id: "b478c479-e0e4-4f5c-93a8-da5e3afc15f3", respuestas: u };
                                                            $("#504f8394-ad32-4ea8-b279-d59a5c9d51d9").show(), $("#b478c479-e0e4-4f5c-93a8-da5e3afc15f3").hide(), b.push(a), $("#" + t).hide();
                                                        });
                                                    } else if ("504f8394-ad32-4ea8-b279-d59a5c9d51d9" === a) {
                                                        j
                                                            .filter(function (e) {
                                                                return "504f8394-ad32-4ea8-b279-d59a5c9d51d9" === e.id;
                                                            })
                                                            .forEach(function (e) {
                                                                e.respuestas.forEach(function (e) {
                                                                    1 == $("#" + e.id).is(":checked") && l.push(e.id);
                                                                });
                                                                var a = { id: "504f8394-ad32-4ea8-b279-d59a5c9d51d9", respuestas: l };
                                                                $("#504f8394-ad32-4ea8-b279-d59a5c9d51d9").hide(), b.push(a), $("#" + t).hide();
                                                            }),
                                                            (i =
                                                                !u.includes("09ba9d8e-ce70-4445-87d4-650a373a0a56") || 1 != u.length || l.includes("daa1f7f2-b7e1-47c8-a0e0-c2ff0098710c") || l.includes("22cf3923-850c-49f6-b0f7-56c3bb9bbbd3")
                                                                    ? "165389f5-161b-47f2-a7f5-20bed053262d"
                                                                    : "7fa462f5-5b8b-46e1-a574-b308607c207f"),
                                                            (e = { fecha: p, diagnostico: i, id_usuario: h, preguntas: b });
                                                    }
                                                    e && (localStorage.setItem("diagnostico", JSON.stringify(e)), $("#reporteGeneral").modal("show"));
                                                },
                                                deseleccion: function (e, a) {
                                                    var t = [];
                                                    t.push(k, w, N, T, I, J);
                                                    var d = 0,
                                                        i = j.filter(function (a) {
                                                            return a.id === e;
                                                        });
                                                    i.forEach(function (e) {
                                                        e.respuestas.forEach(function (e) {
                                                            !0 === $("#" + e.id).is(":checked") &&
                                                                (d++,
                                                                t.forEach(function (a) {
                                                                    e.id === a &&
                                                                        (1 === O
                                                                            ? ($("#" + e.id).prop("checked", !1), (O = 0))
                                                                            : (i.forEach(function (e) {
                                                                                  e.respuestas.forEach(function (e) {
                                                                                      e.id != a && $("#" + e.id).prop("checked", !1);
                                                                                  });
                                                                              }),
                                                                              (O = 1)));
                                                                })),
                                                                d >= 1 ? $("#" + a).prop("disabled", !1) : $("#" + a).prop("disabled", !0);
                                                        });
                                                    });
                                                },
                                                valorDiagnostico: function () {
                                                    var a = {
                                                        url: urlServicio + "/diagnosis/api/v2.0/question",
                                                        method: "POST",
                                                        timeout: 0,
                                                        headers: { "Content-Type": "application/problem+json; charset=utf-8", Authorization: "Bearer " + y },
                                                        data: JSON.stringify(e),
                                                    };
                                                    $.ajax(a).done(function (e) {
                                                        e.error ? console.log("ERROR al guardar en API llamada /question") : console.log("Funciono");
                                                    }),
                                                        $("#" + e.diagnostico).modal("show");
                                                },
                                                valorViaje: function () {
                                                    $("#realizarViaje").modal("show");
                                                },
                                                guardarViaje: function () {
                                                    var e = 1,
                                                        a = "",
                                                        t = !1,
                                                        i = "",
                                                        o = "";
                                                    "Nacional" == document.getElementById("tipoVuelo").value && (t = !0);
                                                    var n = {
                                                        transport_mode_id: e,
                                                        airline_id: document.getElementById("aerolinea").value,
                                                        company_name: a,
                                                        ship: document.getElementById("nVuelo").value,
                                                        seat: document.getElementById("nSilla").value,
                                                        is_domestic: t,
                                                        travel_date: document.getElementById("fechaVuelo").value,
                                                        origin_mun: i,
                                                        destination_mun: o,
                                                    };
                                                    if ("" != n.travel_date && "" != n.ship && "" != n.seat) {
                                                        var r = {
                                                            url: urlServicio + "/diagnosis/api/v1.0/travel/createtravelrecord",
                                                            method: "POST",
                                                            timeout: 0,
                                                            headers: { "Content-Type": "application/problem+json; charset=utf-8", Authorization: "Bearer " + y },
                                                            data: JSON.stringify(n),
                                                        };
                                                        $.ajax(r).done(function (e) {
                                                            (n.aerolinea = d.responseJSON.data.find(function (e) {
                                                                return e.id == n.airline_id;
                                                            }).name),
                                                                localStorage.setItem("viaje", JSON.stringify(n)),
                                                                (location.href = "codigoQR-coronApp.html");
                                                        });
                                                    } else {
                                                        var c = document.getElementById("alertViaje");
                                                        c.parentElement.style.right = "0px";
                                                        var s = n.travel_date.split("-");
                                                        new Date(s[0], s[1] - 1, s[2]) < new Date(new Date().getFullYear(), new Date().getMonth(), new Date().getDate())
                                                            ? (c.textContent = "La fecha del vuelo no puede ser anterior que la fecha actual.")
                                                            : (n.seat || (c.textContent = "Por favor ingrese el número de su asiento."),
                                                              n.ship || (c.textContent = "Por favor ingrese el número de su vuelo."),
                                                              n.travel_date || (c.textContent = "Por favor seleccione una fecha de viaje."));
                                                    }
                                                },
                                            },
                                        });
                                    }
                                    t.done(function () {
                                        i();
                                    });
                                })();
                            });
                        });
                    });
            },
            datos = JSON.parse(informuser),
            lastUserSet = {
                url: urlServicio + "/passport/api/v1.0/QR/last/user/" + datos.user.id,
                method: "GET",
                timeout: 0,
                headers: { "Content-Type": "application/problem+json; charset=utf-8", Authorization: "Bearer " + datos.bearer_token },
            };
        $.ajax(lastUserSet).done(function (e) {
            total(e);
        });
    } else location.href = "registro-coronApp.html";
}
//# sourceMappingURL=mainCoronApp.js.map
