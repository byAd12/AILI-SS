//////////////////////////////////////////////////////////////////////
// PONER UNA CLASE AL LLEGAR AL PRINCIPIO

function handleStickyBackground() {
    const stickyElement = document.querySelector('.menú');
    
    function toggleStickyBackground() {
        const elementTop = stickyElement.getBoundingClientRect().top;
        if (elementTop <= 0) {
            stickyElement.classList.add('active');
        } else {
            stickyElement.classList.remove('active');
        }
    }

    // Asegúrate de que el evento se registre correctamente.
    window.addEventListener('scroll', toggleStickyBackground);
}
handleStickyBackground();

//////////////////////////////////////////////////////////////////////
// FILTROS DE DESCARGAS

document.addEventListener("DOMContentLoaded", function() {
    try{
        const versionesContainer = document.querySelector(".InfoVersiones"),
        filtrosVersiones = document.querySelector(".FiltrosVers"),
        filtrosEspac = document.querySelector(".FiltrosEspac"),
        filtrosFechas = document.querySelector(".FiltroFechas"),
        filtrosFechaSubida = document.querySelector(".FiltroFechaSubida"),
        filtrosTamañoDisco = document.querySelector(".FiltroFechas"),
        versiones = [];

        versionesContainer.querySelectorAll(".VersionesDESCARGA").forEach(versionEl => {
            const titulo = versionEl.querySelector("h3").textContent,
                    fecha = versionEl.querySelector("p span").textContent,
                    spans = versionEl.querySelectorAll("p span"),
                    tamaño = spans.length > 1 ? spans[1].textContent : "",
                    match = titulo.match(/Versión ([\d.]+) - (Windows|Linux)/);

            if (match) {
                const version = match[1], tipo = match[2];
                versiones.push({ version, tipo, fecha, tamaño, element: versionEl });
            }
        });

        function updateVisibility(versionFilter, typeFilter, dateFilter, uploadDateFilter, sizeFilter) {
            versiones.forEach(({ version, tipo, fecha, tamaño, element }) => {
                const matchVersion = !versionFilter || version === versionFilter,
                        matchTipo = !typeFilter || tipo === typeFilter,
                        matchFecha = !dateFilter || fecha === dateFilter,
                        matchUploadDate = !uploadDateFilter || fecha === uploadDateFilter,
                        matchSize = !sizeFilter || tamaño === sizeFilter;
                element.style.display = (matchVersion && matchTipo && matchFecha && matchUploadDate && matchSize) ? "" : "none";
            });
        }

        const uniqueVersiones = [...new Set(versiones.map(v => v.version))],
                uniqueTipos = [...new Set(versiones.map(v => v.tipo))],
                uniqueFechas = [...new Set(versiones.map(v => v.fecha))],
                uniqueTamaños = [...new Set(versiones.map(v => v.tamaño))];

        uniqueVersiones.forEach(version => {
            const link = document.createElement("a");
            link.href = "#";
            link.textContent = version;
            link.addEventListener("click", (e) => { e.preventDefault(); updateVisibility(version, null, null, null, null); });
            filtrosVersiones.appendChild(link);
        });

        uniqueTipos.forEach(tipo => {
            const link = document.createElement("a");
            link.href = "#";
            link.textContent = tipo;
            link.addEventListener("click", (e) => { e.preventDefault(); updateVisibility(null, tipo, null, null, null); });
            filtrosEspac.appendChild(link);
        });

        uniqueFechas.forEach(fecha => {
            const link = document.createElement("a");
            link.href = "#";
            link.textContent = fecha;
            link.addEventListener("click", (e) => { e.preventDefault(); updateVisibility(null, null, fecha, null, null); });
            filtrosFechaSubida.appendChild(link);
        });

        uniqueTamaños.forEach(tamaño => {
            const link = document.createElement("a");
            link.href = "#";
            link.textContent = tamaño;
            link.addEventListener("click", (e) => { e.preventDefault(); updateVisibility(null, null, null, null, tamaño); });
            filtrosTamañoDisco.appendChild(link);
        });

        document.querySelector(".Filtros h2").addEventListener("click", () => { updateVisibility(null, null, null, null, null); });
    } catch{}
});

//////////////////////////////////////////////////////////////////////
// ENLACES EXTERNOS

document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll("a[href*='?link=']").forEach(link => {
        link.addEventListener("click", event => {
            event.preventDefault();
            const params = new URLSearchParams(link.search);
            let externalUrl = params.get("link");
            if (externalUrl === "MEGA1") {externalUrl = "https://mega.nz/file/dKtzjSAD#z-Br1TNuEndBqBtD_gK0Rfqw1wTu6Tbjl74dNV1Ca78";}
            if (externalUrl === "GIT1") {externalUrl = "https://github.com/byAd12/AILI-SS/releases/tag/win-1.0";}

            if (externalUrl === "MEGA2") {externalUrl = "https://mega.nz/file/Va8zwQAL#FBBefM7Ql9o60d1rwoX6xQx4SK4_-ZHNkNeglSCE_qs";}
            if (externalUrl === "GIT2") {externalUrl = "https://github.com/byAd12/AILI-SS/releases/tag/win-1.1";}

            if (externalUrl === "MEGA3") {externalUrl = "https://mega.nz/file/AKUQHJiJ#CMfrkkkgkXMB31WOBzgkeidg5tPHkxM8eiTFnRb332Y";}
            if (externalUrl === "GIT3") {externalUrl = "https://github.com/byAd12/AILI-SS/releases/tag/win-1.2";}

            if (externalUrl === "MEGA4") {externalUrl = "https://mega.nz/file/oS0AwYjb#nj_xkDg1KRma5TjuCGNbqFI_5wTy6ReFaLFud4IZo1w";}
            if (externalUrl === "GIT4") {externalUrl = "https://github.com/byAd12/AILI-SS/releases/tag/win-1.3";}

            if (externalUrl === "MEGA5") {externalUrl = "https://mega.nz/file/FWlzhCiA#KCFX03Uf_pWPKigVDiPwGKDnEDgl91FdZOG7CD5Cqr0";}
            if (externalUrl === "GIT5") {externalUrl = "https://github.com/byAd12/AILI-SS/releases/tag/win-1.4";}

            if (externalUrl === "MEGA6") {externalUrl = "https://mega.nz/file/RbV2UDaR#PzadBUFzdwyumyOmuTWZ2yzY94MceoEHvpVvYcS5XMM";}
            if (externalUrl === "GIT6") {externalUrl = "https://github.com/byAd12/AILI-SS/releases/tag/win-1.5";}

            if (externalUrl === "MEGA7") {externalUrl = "https://mega.nz/file/9KMDESDD#gFZuYXXbhDxf--9X8Qc0pWQaGpSP6U_HFC_nJcgAhgA";}
            if (externalUrl === "GIT7") {externalUrl = "https://github.com/byAd12/AILI-SS/releases/tag/win-1.6";}

            if (externalUrl === "MEGA8") {externalUrl = "https://mega.nz/file/VP9GkBbQ#xqnaTVlmewvzUSBWPLPg_AOKpV-Xg6Pm5mOgBO8tu0c";}
            if (externalUrl === "GIT8") {externalUrl = "https://github.com/byAd12/AILI-SS/releases/tag/v1.7";}

            if (externalUrl === "MEGA9") {externalUrl = "https://mega.nz/file/QXcBmYKT#-nK7HEOl_P4H2fqVVC-RbwSGGNjWIxskz6l03qeJbOs";}
            if (externalUrl === "GIT9") {externalUrl = "https://github.com/byAd12/AILI-SS/releases/tag/v1.7";}

            if (externalUrl === "MEGA10") {externalUrl = "https://mega.nz/file/IK1VFCJb#6cnU_oD4cX3NrTB9guMzZsuEGEOX2ni1GWUsZeyk6Vk";}
            if (externalUrl === "GIT10") {externalUrl = "https://github.com/byAd12/AILI-SS/releases/tag/v2.0";}

            if (externalUrl === "MEGA11") {externalUrl = "https://mega.nz/file/BOtnhJga#wmiYHhpqVQ_RVK7R2JUPoJyzC9f2McisVQQvkeBXzqQ";}
            if (externalUrl === "GIT11") {externalUrl = "https://github.com/byAd12/AILI-SS/releases/tag/v2.0";}

            if (externalUrl === "MEGA12") {externalUrl = "https://mega.nz/file/JGN3ADKZ#oC_V7jHyPqSqaSstfd6KT1DufxLOYUJgBiAHy7tuSmE";}
            if (externalUrl === "GIT12") {externalUrl = "https://github.com/byAd12/AILI-SS/releases/tag/v2.0";}


            window.open(externalUrl, "_blank");
        });
    });
});

//////////////////////////////////////////////////////////////////////
// QUITAR EL ID EN LA FLECHA

function QuitarID(event) {
    setTimeout(() => {
        history.pushState("", document.title, window.location.pathname);
    }, 1);
}

//////////////////////////////////////////////////////////////////////
// Enseñar/Ocutlar los DAFO personales en contacto mediante click en un botón o pantalla

function EnsenarDAFO(cual){
    document.getElementById("DAFO_PERSONALES").style.display = "inherit";
    document.body.style.overflow = "hidden";
    document.getElementById("fondoOscuro").style.display = "block";
    if (cual == 1){
        document.getElementById("AdDAFO").style.display = "inherit";
    } if (cual == 2){
        document.getElementById("IvDAFO").style.display = "inherit";
    } if (cual == 3){
        document.getElementById("LuDAFO").style.display = "inherit";
    } if (cual == 4){
        document.getElementById("IsDAFO").style.display = "inherit";
    }
}

function CerrarDAFO() {
    document.getElementById("DAFO_PERSONALES").style.display = "none";
    document.body.style.overflow = "inherit";
    document.getElementById("fondoOscuro").style.display = "none";
    document.getElementById("AdDAFO").style.display = "none";
    document.getElementById("IvDAFO").style.display = "none";
    document.getElementById("LuDAFO").style.display = "none";
    document.getElementById("IsDAFO").style.display = "none";
}

//////////////////////////////////////////////////////////////////////
// Animar .parte1

function animarLetras() {
    document.querySelectorAll(".parte1 h1 .letra").forEach((letra, index) => {
        setTimeout(() => {
            letra.style.animation = "subirBajar 0.5s ease-in-out";
            letra.addEventListener("animationend", () => {letra.style.animation = "";}, { once: true });
        }, index * 300);
    });
}

function animarLetrassignificado() {
    document.querySelectorAll(".Significado1 .letra").forEach((letra, index) => {
        setTimeout(() => {
            letra.style.animation = "cambiarbordersignificado 0.5s ease-in-out";
            letra.addEventListener("animationend", () => {letra.style.animation = "";}, { once: true });
        }, index * 300);
    });
}

animarLetras();
animarLetrassignificado();
setInterval(animarLetras, 5000);
setInterval(animarLetrassignificado, 5000);

//////////////////////////////////////////////////////////////////////
// Animar linea de trabajo

window.onload = function() {
    function animarlineatrabajoprincipal() {
        document.querySelectorAll(".Mom h3").forEach((elemento, index) => {
            const icono = elemento.querySelector(".icon");
            const fecha = elemento.querySelector(".fechaMom");

            setTimeout(() => {
                if (fecha) {fecha.style.opacity = "1"; fecha.style.transition = "opacity 0.3s ease";}
                if (icono) {icono.style.color = "red";}

                if (fecha || icono) {
                    elemento.addEventListener("animationend", () => {
                        if (fecha) fecha.style.animation = "";
                        if (icono) icono.style.animation = "";
                    }, { once: true });}}, index * 300);});
    }

    document.querySelectorAll(".Mom h3").forEach(elemento => {
        const icono = elemento.querySelector(".icon");
        const fecha = elemento.querySelector(".fechaMom");
        if (fecha) fecha.style.opacity = "0";
        if (icono) icono.style.color = "white";
    });

    animarlineatrabajoprincipal();

    function animarlineatrabajo() {
        document.querySelectorAll(".Mom h3 .icon").forEach((icono, index) => {
            setTimeout(() => {
                icono.style.color = (icono.style.color === "red") ? "#007bff" : "red";
                icono.addEventListener("animationend", () => { icono.style.animation = ""; }, { once: true });
            }, index * 300);
        });
    }
    setInterval(animarlineatrabajo, 4000);
};

//////////////////////////////////////////////////////////////////////
// FAQ

function ensenarFAQpr(elemento) {
    document.querySelectorAll(".PreguntaPRODUC ol li").forEach(el => {el.style.display = "none";});
    document.querySelectorAll(".PreguntaPRODUC h2").forEach(el => {el.style.margin = "0 0 0 0";});

    let lista = elemento.querySelectorAll("ol li");
    let titulo = elemento.querySelector("h2");
    
    if (lista.length > 0) {lista.forEach(li => {li.style.display = "block";});}
    if (titulo) {titulo.style.margin = "0 0 30px 0";}
}

//////////////////////////////////////////////////////////////////////
// Mira automáticamente si está en caché el modo oscuro o claro

document.addEventListener("DOMContentLoaded", function() {
    let savedMode = localStorage.getItem("mode");
    if (savedMode === "light") {document.body.dataset.mode = "light";}
    else {applyDarkMode();}
});

//////////////////////////////////////////////////////////////////////
// Qué hacer cuando se pulsa el botón de modo oscuro

function toggleMode() {
    let body = document.body;
    
    if (body.dataset.mode === "dark") {
        localStorage.setItem("mode", "light");
        body.dataset.mode = "light";

        try {
            document.querySelectorAll('h2').forEach(element => {element.classList.remove('add-after');});
            document.querySelector('.PlanEmpresa img').classList.remove('im_plan');
        } catch {}
        location.reload();
    } else {
        localStorage.setItem("mode", "dark");
        applyDarkMode();
    }
}

//////////////////////////////////////////////////////////////////////
// Aplicar el modo oscuro a todos los elementos

function applyDarkMode() {
    let body = document.body;
    let elements = document.querySelectorAll('*:not(.parte1 *, .NoCambiarColor, .AfterFooter, .AfterFooter span, .BotonContactarPrecios, .AnadirChrome, .PreciosFlex hr, .TodoTERMINOS h3 span, .SubrayarLegal:not(.UsoLogo .SubrayarLegal), .AnuncioPt1 *, footer *, .logo h1 span, .TUTOTIAL2separarA a, .z100 a, .carrusel-item, .TUTOTIAL p a, .IndiceGlobal a, .VersionesDESCARGA div a, .TUTOTIAL2 div a, .DIVLinks a, .Parte1404 *');
    let registros_links = document.querySelectorAll('.z100 a');
    let h2_after = document.querySelectorAll('h2:not(.ClaveGratuitaLogo)');
    let im_plan = document.querySelectorAll('.PlanEmpresa img');
    let EnlNuevo = document.querySelectorAll('.EnlNuevo');
    let UsoLogo2 = document.querySelectorAll('.UsoLogo');
    let filtros_a = document.querySelectorAll('.Filtros a');
    let p_a = document.querySelectorAll('.PreguntaPRODUC a, p a:not(.AnuncioPt1 a, .VersionesDESCARGA p a, footer p a, .Mom p a, .advertenciaH2CLAVE a, .Donaciones a, .CréditosImagen a)');
    let filtros = document.querySelector('.Filtros');
    let Mom = document.querySelectorAll('.Mom');
    let prevz = document.querySelector('.prevz img:not(.PythonLogoDescargas)');
    let extension_muestra = document.querySelector('.muestraa');
    let descarga_div_a = document.querySelectorAll('.VersionesDESCARGA div a:not(.VersionesDESCARGA div p a), .TodoDESC div div div');
    let border_azuk = document.querySelectorAll('.PreciosFlex div:not(.PreciosFlex div div), .AQuienNosDirigimosFlex div, .TodoTERMINOS hr, .flexEMAILS div:not(.flexEMAILS div *), .PreguntasPRODUC div div');
    let menu = document.querySelector('.menú');
    let chrome_logo = document.querySelector('#CambiarChromeANegro');
    let CambiarWinANegro = document.querySelector('#CambiarWinANegro');
    let CambiarLinANegro = document.querySelector('#CambiarLinANegro');
    let subrayar = document.querySelectorAll('.SubrayarLegal:not(.UsoLogo .SubrayarLegal)');
    let cambiar_legal1 = document.querySelectorAll('.EnlNuevo a');
    let menu_botones = document.querySelectorAll('.menú div ul a li, .menú div ul a span');
    let faq_todo_conj = document.querySelectorAll('.PreguntaPRODUC .hoverA');
    let terminos_h3_span = document.querySelectorAll('.TodoTERMINOS h3 span');
    let BotonContactarPrecios = document.querySelectorAll('.BotonContactarPrecios');
    let PreciosFlexHR = document.querySelectorAll('.PreciosFlex hr');

    menu_botones.forEach(element => {
        element.addEventListener('mouseenter', () => {element.style.backgroundColor = "rgba(0, 123, 255, 0.2)";});
        element.addEventListener('mouseleave', () => {element.style.backgroundColor = " rgb(36,36,36)"});
    });

    Mom.forEach(element => {
        element.addEventListener('mouseenter', () => {element.style.borderTop = "3px solid blue";});
        element.addEventListener('mouseleave', () => {element.style.borderTop = " 3px solid white"});
    });

    PreciosFlexHR.forEach(element => {element.style.border = "1px solid rgb(141, 141, 216)";});
    BotonContactarPrecios.forEach(element => {element.style.backgroundColor = "white !important";});
    faq_todo_conj.forEach(element => {element.style.border = "1px solid white !important";});
    p_a.forEach(element => {element.style.borderBottom = "3px solid blue";});
    p_a.forEach(element => {element.style.borderLeft = "3px solid blue";});
    filtros_a.forEach(element => {element.style.border = "1px solid rgb(226, 213, 213)";});
    descarga_div_a.forEach(element => {element.style.border = "1px solid rgb(226, 213, 213)";});
    EnlNuevo.forEach(element => {element.classList.add('EnlNuevo2');});
    UsoLogo2.forEach(element => {element.classList.add('UsoLogo2');});
    h2_after.forEach(element => {element.classList.add('add-after');});
    border_azuk.forEach(el => {el.style.border = "1px solid blue";});
    cambiar_legal1.forEach(el => {el.style.color = "white";});
    registros_links.forEach(el => {el.style.backgroundColor = "rgb(147, 147, 247)";});
    terminos_h3_span.forEach(el => {el.style.color = "rgb(147, 147, 247)";});
    registros_links.forEach(el => {el.style.color = "black";});
    Mom.forEach(el => {el.style.borderTop = "3px solid white";});

    im_plan.forEach(element => {element.classList.add('im_plan');});
    body.style.backgroundColor = "rgb(36,36,36)";
    try {extension_muestra.src = "Img/Extension/Extension_Muestra_Oscuro.png";} catch {}
    try {chrome_logo.src = "Img/Extension/ChromeBlanco.png";} catch {}
    try {CambiarWinANegro.src = "Img/Logos/AvailableInWindowsBlanco.png";} catch {}
    try {CambiarLinANegro.src = "Img/Logos/DescargarLinuxBlanco.svg";} catch {}
    body.style.color = "white";
    menu.style.backgroundImage = 'none';
    menu.style.backgroundColor = "rgb(36,36,36)";
    
    if (prevz) {
        prevz.style.filter = 'brightness(120%)';
        prevz.style.borderRadius = '10px';
        prevz.classList.add('prevzimg');
    }

    elements.forEach(el => {
        el.style.backgroundColor = "rgb(36,36,36)";
        el.style.color = "white";
    });
    
    try {filtros.style.borderLeft = "1px solid white";} catch {}
    try {subrayar.forEach(element => {element.style.backgroundColor = "rgba(61, 59, 59, 0.3)";});} catch {}
    try {document.getElementById("Organigrama").src = "Img/Empresa/Organigrama-Empresa-2.jpg";} catch {}

    body.dataset.mode = "dark";
}

//////////////////////////////////////////////////////////////////////
// Cuando en móviles se ponga el toggle del menú se enseñará todo

function ensenarmenumov() {
    document.querySelector(".NoBorde ul").classList.toggle("active");

    const menuboton = document.querySelector(".NoBorde ul a");
    if (menuboton.classList.contains("menucc")) {
        if (menuboton.classList.contains("active")){
            menuboton.innerHTML = "Cerrar menú";
        } else {menuboton.innerHTML = "Menú";}
    }
}

//////////////////////////////////////////////////////////////////////
// Cuando se ponga cualquier bloque en la vista se enseñará y se desplazará hacia arriba

document.addEventListener("DOMContentLoaded", function() {
    const blocks = document.querySelectorAll('.block');

    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('show');
                observer.unobserve(entry.target);
            }
        });
    }, {threshold: 0.2});

    blocks.forEach(block => {observer.observe(block);});
});

//////////////////////////////////////////////////////////////////////
// Cuando se haga scroll en index.html se moverá a la derecha en backgroundImage

window.addEventListener('scroll', () => {
    try{document.getElementById("parte1").style.backgroundPosition = `${window.scrollY * 0.2}px 0px`;} catch{}
});

//////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////