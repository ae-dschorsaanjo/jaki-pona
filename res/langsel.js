const EN_SEL = document.getElementById("en");
const HU_SEL = document.getElementById("hu");
const EN_ID = EN_SEL.id;
const HU_ID = HU_SEL.id;
const sel = id => { if (id == HU_ID) return HU_SEL; else return EN_SEL; };
const SEL_CLS = "sel";
const MAIN_PREFIX = "main-";
const LANG = "lang";

function hideMain(lang) {
    let [on, off] = lang == EN_ID ? [EN_ID, HU_ID] : [HU_ID, EN_ID];
    document.getElementById(MAIN_PREFIX + on).style.display = 'block';
    document.getElementById(MAIN_PREFIX + off).style.display = 'none';
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

chooseLanguage(EN_ID, true);