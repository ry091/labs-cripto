// ==UserScript==
// @name         este si
// @namespace    http://tampermonkey.net/
// @version      2024-06-07
// @description  try to take over the world!
// @author       You
// @match        https://cripto.tiiny.site/
// @icon         data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==
// @grant        none
// @require      https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.1.1/crypto-js.min.js#sha512-E8QSvWZ0eCLGk4km3hxSsNmGWbLtSCSUcewDQPQWZF6pEU8GlT8a5fF32wOl1i8ftdMhssTrF/OhyGWwonTcXA==

// ==/UserScript==

(function() {
    'use strict';

    let claveGlobal = "";

    function mayusculas(text) {
        return text.match(/[A-Z]/g) || [];
    }

    function ajustarClave(clave) {
        const longitudDeseada = 24;
        if (clave.length < longitudDeseada) {
            while (clave.length < longitudDeseada) {
                clave += clave;  // Repetir la clave para alcanzar la longitud deseada
            }
        }
        return clave.substring(0, longitudDeseada);
    }

    // Función para cifrar y descifrar
    function cifrarMensaje(mensaje, llave) {
        llave = ajustarClave(llave);  // Ajustar la longitud de la clave antes de cifrar
        let claveHex = CryptoJS.enc.Utf8.parse(llave);
        return CryptoJS.TripleDES.encrypt(mensaje, claveHex, {
            mode: CryptoJS.mode.ECB,
            padding: CryptoJS.pad.Pkcs7
        }).toString();
    }

    function descifrarMensaje3DES(mensajeCifradoBase64, clave) {
        clave = ajustarClave(clave);  // Ajustar la longitud de la clave antes de descifrar
        let claveHex = CryptoJS.enc.Utf8.parse(clave);
        let mensajeDescifrado = CryptoJS.TripleDES.decrypt({
            ciphertext: CryptoJS.enc.Base64.parse(mensajeCifradoBase64)
        }, claveHex, {
            mode: CryptoJS.mode.ECB,
            padding: CryptoJS.pad.Pkcs7
        });
        return mensajeDescifrado.toString(CryptoJS.enc.Utf8);
    }

    // Función para imprimir mensajes en la página
    function imprimirMensajesEnPagina(mensajeCifrado, mensajeDescifrado) {
        let div = document.createElement('div');
        div.textContent = `${mensajeCifrado} : ${mensajeDescifrado}`;
        document.body.appendChild(div);
    }

    // Función para buscar y mostrar la contraseña (clave)
    function buscarYMostrarContraseña() {
        var allText = document.body.innerText;
        var upperCaseLetters = mayusculas(allText);
        claveGlobal = ajustarClave(upperCaseLetters.join(''));
        console.log('La llave es:', claveGlobal);
    }

    // Función para contar los mensajes cifrados y descifrarlos
    function descifrarTodosLosMensajes() {
        let divs = document.querySelectorAll("div[id]");
        console.log('Los mensajes cifrados son:', divs.length);

        divs.forEach(div => {
            let mensajeCifradoBase64 = div.id;
            if (mensajeCifradoBase64) {
                let mensajeDescifrado = descifrarMensaje3DES(mensajeCifradoBase64, claveGlobal);
                console.log(`${mensajeCifradoBase64} : ${mensajeDescifrado}`);
                imprimirMensajesEnPagina(mensajeCifradoBase64, mensajeDescifrado);
            }
        });
    }

    // Función para cambiar el contenido de la página
    function cambiarContenido() {
        var elementosP = document.querySelectorAll('p');

        elementosP.forEach(function(p) { // Elimina los campos <p>
            p.remove();
        });

        var elementosDiv = document.querySelectorAll('div');

        elementosDiv.forEach(function(div) { // Elimina los campos <div>
            div.remove();
        });

        var nuevoT = document.createElement('p');
        nuevoT.textContent = 'Después de Escuchar historias Sobre Exploradores, Pablo decidió Empezar su propia aventura. Recorriendo Tierras distantes, Apreció la Riqueza de la naturaleza. En cada lugar que Visitó, Impresionantes paisajes Se revelaban ante sus ojos. Intrigado por las Tradiciones locales, Aprendió mucho de los pueblos que Visitaba. Incluso en situaciones Adversas, Nunca perdió la esperanza. Todas estas experiencias Enriquecieron su vida, Sin duda alguna';
        document.body.appendChild(nuevoT);

        var mCifrados = ['G2oLJ8yuXQY=', 'PjFwP6jHWWU=', 'vdi/Iv4N3fE='];

        for (var i = 0; i < mCifrados.length; i++) {
            var nuevoDiv = document.createElement('div');
            nuevoDiv.id = mCifrados[i];
            nuevoDiv.className = 'm' + i.toString();
            document.body.appendChild(nuevoDiv);
        }
    }

    // Esperar hasta que el DOM esté completamente cargado
    window.addEventListener('load', () => {
        cambiarContenido();
        setTimeout(() => {
            buscarYMostrarContraseña();
            descifrarTodosLosMensajes();
        }, 1000); // 1 segundo de retraso para asegurarse de que el DOM se ha actualizado
    });
})();