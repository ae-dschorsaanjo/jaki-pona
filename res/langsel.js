const EN_SEL = document.getElementById("en");
const HU_SEL = document.getElementById("hu");
const EN_ID = EN_SEL.id;
const HU_ID = HU_SEL.id;
const sel = id => { if (id == HU_ID) return HU_SEL; else return EN_SEL; };
const SEL_CLS = "sel";
const MAIN_PREFIX = "main-";
const LANG = "lang";
const SBS_CLS = "sbs";

function setDisplay(target, value) {
    document.getElementById(MAIN_PREFIX + target).style.display = value;
}

function hideMain(lang) {
    let [on, off] = lang == EN_ID ? [EN_ID, HU_ID] : [HU_ID, EN_ID];
    setDisplay(on, 'block');
    setDisplay(off, 'none');
    sel(on).classList.add(SEL_CLS);
    sel(off).classList.remove(SEL_CLS);
}

function chooseLanguage(lang, first_call = false) {
    if (first_call) {
        let storedLang = localStorage.getItem(LANG);
        if (storedLang) lang = storedLang;
    }
    else {
        if (localStorage.getItem(LANG) == lang) return false;
        localStorage.setItem(LANG, lang);
    }
    hideMain(lang);
    return true;
}

EN_SEL.addEventListener("click", e => {
    chooseLanguage(EN_ID);
});

HU_SEL.addEventListener("click", e => {
    chooseLanguage(HU_ID);
})

document.addEventListener("keydown", (event) => {
    if (event.altKey) {
        switch (event.key) {
            case "a":
            case "e":
                event.preventDefault();
                chooseLanguage(EN_ID);
                break;
            case "h":
            case "m":
                event.preventDefault();
                chooseLanguage(HU_ID);
                break;
            case "s":
                event.preventDefault();
                let cl = document.body.classList;
                if (cl.contains(SBS_CLS)) {
                    cl.remove(SBS_CLS);
                    chooseLanguage(EN_ID, true);
                }
                else {
                    cl.add(SBS_CLS);
                    setDisplay(EN_ID, "block");
                    setDisplay(HU_ID, "block");
                }
                break;
        }
    }
});

chooseLanguage(EN_ID, true);

// TODO: update URL based on language selection and be able to
//       read selected language from URL