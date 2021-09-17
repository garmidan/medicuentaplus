"use strict"; localStorage.setItem("sesion", "false"), localStorage.clear(); var recaptcha, informacionusuario = {}, urlServicio = "https://apicovidqa.and.gov.co", settings = { url: "https://countriesnow.space/api/v0.1/countries/codes", method: "GET", timeout: 0 }; $.ajax(settings).done((function (e) { var t = /[\s\+]/gi, n = document.getElementById("indicativo"); for (var o in e.data) "+57" != e.data[o].dial_code && (n.options[n.options.length] = new Option(e.data[o].dial_code, e.data[o].dial_code.replace(t, ""))) })), document.getElementById("register").addEventListener("click", (function (e) { e.preventDefault(); var t = document.getElementById("nombre").value, n = document.getElementById("apellido").value, o = document.getElementById("tipodoc").value, a = document.getElementById("ndoc").value, r = document.getElementById("mail").value, i = document.getElementById("ncel").value, l = document.getElementById("indicativo").value, c = document.getElementById("pass").value, s = document.getElementById("gridCheck").checked, d = document.getElementById("alertregister"); if (0 == grecaptcha.getResponse().length) d.parentElement.style.right = "0px", d.textContent = "Verifique el recaptcha"; else if (t && n && o && a && s && r && c) { var u = { document_type: o, document_number: a, firstname: t, lastname: n, email: r, password: c, phone: i, phone_area_code: l, recaptcha_token: recaptcha }; fetch(urlServicio + "/api/v2.0/authentication/register", { method: "POST", body: JSON.stringify(u), headers: { "Content-Type": "application/json" } }).then((function (e) { return e.json() })).catch((function (e) { return console.log("Error: " + e) })).then((function (e) { void 0 !== e.errors && void 0 !== e.errors.Password ? (d.parentElement.style.right = "0px", d.textContent = "La contraseña no puede estar vacia. Debe tener al menos 6 caracteres,una letra mayúscula, una letra minúscula,un número y un símbolo.") : void 0 !== e.errors && void 0 !== e.errors.Email ? (d.parentElement.style.right = "0px", d.textContent = "El email no puede estar vacío y debe ser una dirección válida.") : void 0 !== e.status ? (d.parentElement.style.right = "0px", d.textContent = "Error en los datos proporcionados.") : !0 === e.error ? (console.log(e), d.parentElement.style.right = "0px", d.textContent = e.message) : (document.getElementById("verifica").style.display = "block", document.getElementById("register").style.display = "none") })) } else d.parentElement.style.right = "0px", s || (d.textContent = "Debe aceptar los terminos y condiciones."), c || (d.textContent = "Por favor ingrese una contraseña"), r || (d.textContent = "Por favor ingrese su correo electronico"), a || (d.textContent = "Por favor ingrese su número de documento."), n || (d.textContent = "Por favor ingrese su apellido."), t || (d.textContent = "Por favor ingrese su nombre.") })); var verifyCallback = function (e) { recaptcha = e }, onloadCallback = function () { grecaptcha.render("recaptcha", { sitekey: "6Lc_wt8ZAAAAABD-b95vbqaVyDWwjqJ-zxenPU-X", callback: verifyCallback }), console.log(grecaptcha.getResponse()) }, queryString2 = window.location.search, urlParams2 = new URLSearchParams(queryString2), email2 = urlParams2.get("email"), token2 = urlParams2.get("tokenPW"); email2 && token2 && $("#cambioClaveModal").modal("show"), document.getElementById("cambioClave").addEventListener("click", (function (e) { e.preventDefault(); var t = document.getElementById("pass1").value, n = document.getElementById("pass2").value, o = document.getElementById("alertVerificoClave"); if (t != n) o.parentElement.style.right = "0px", o.textContent = "Contraseñas no coinciden"; else if (t && n) { var a = { url: urlServicio + "/api/v2.0/authentication/changepassword", method: "POST", timeout: 0, headers: { "Content-Type": "application/problem+json; charset=utf-8" }, data: '{"email": "' + email2 + '",   "token": "' + token2 + '", "password": "' + t + '"}' }; $.ajax(a).done((function (e) { e.success && ($("#loginModal").addClass("disable"), $("#cambioClaveModal").modal("hide"), $("#contrasenaCambiada").modal("show")), e.error && (o.parentElement.style.right = "0px", o.textContent = "Link vencido", setTimeout((function () { location = location.href.split("?")[0] }), 3e3)) })).fail((function (e) { o.parentElement.style.right = "0px", o.textContent = "La contraseña no puede estar vacia. Debe tener al menos 6 caracteres,una letra mayúscula, una letra minúscula,un número y un símbolo." })) } else n || (o.parentElement.style.right = "0px", o.textContent = "Por favor confirme su contraseña"), t || (o.parentElement.style.right = "0px", o.textContent = "Por favor ingrese una contraseña") })); var queryString = window.location.search, urlParams = new URLSearchParams(queryString), email = urlParams.get("email"), token = urlParams.get("token"); if (email && token) { var url = urlServicio + "/api/v2.0/authentication/verifyemail", data = { email: email, token: token }; fetch(url, { method: "POST", body: JSON.stringify(data), headers: { "Content-Type": "application/json" } }).then((function (e) { return e.json() })).catch((function (e) { return console.error("Error:", e) })).then((function (e) { var t = document.getElementById("alertregister"); !0 === e.error ? (t.parentElement.style.right = "0px", t.textContent = "Token no coincide") : (informacionusuario = e, localStorage.setItem("informacionusuario", JSON.stringify(informacionusuario)), location.href = "diagnostico-coronApp.html", localStorage.setItem("sesion", !0)) })) } document.getElementById("login").addEventListener("click", (function (e) { e.preventDefault(); var t = { email: document.getElementById("maillogin").value, password: document.getElementById("passlogin").value }; fetch(urlServicio + "/api/v2.0/authentication/login", { method: "POST", body: JSON.stringify(t), headers: { "Content-Type": "application/json" } }).then((function (e) { return e.json() })).catch((function (e) { console.error("Error: Esta entrando al error", e) })).then((function (e) { informacionusuario = e; var t = document.getElementById("alert"); informacionusuario.status || !0 === informacionusuario.error ? (t.parentElement.style.right = "0px", t.textContent = "Verifique sus datos") : (localStorage.setItem("informacionusuario", JSON.stringify(informacionusuario)), location.href = "diagnostico-coronApp.html", localStorage.setItem("sesion", !0)) })) })), document.getElementById("recuperar").addEventListener("click", (function (e) { e.preventDefault(), $("#loginModal").modal("hide"); var t = document.getElementById("mailloginRec").value, n = { url: urlServicio + "/api/v2.0/authentication/recoverpassword", method: "POST", timeout: 0, headers: { "Content-Type": "application/problem+json; charset=utf-8" }, data: '{"email": "' + t + '"}' }; $.ajax(n).done((function (e) { if (e.success && ($("#recuperacionPW").modal("hide"), $("#envioMailRecuperacion").modal("show")), e.error) { var t = document.getElementById("alertDatos"); t.parentElement.style.right = "0px", t.textContent = "Correo no registrado." } })) })), document.getElementById("envioCorreoCorrecto").addEventListener("click", (function (e) { e.preventDefault(), location.reload() })), document.getElementById("cambioContrasenaExitoso").addEventListener("click", (function (e) { e.preventDefault(), location = location.href.split("?")[0] }));
//# sourceMappingURL=register.js.map