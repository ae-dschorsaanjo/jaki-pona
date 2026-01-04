const EN_ID = "en";
const HU_ID = "hu";
const SEL_CLS = "sel";
const MAIN_PREFIX = "main-";
const LANG = "lang";
const SBS_CLS = "sbs";
const BLOCK = "block";
const NONE = "none";

class LangSel {
    #selector;
    static all = {};
    get elem() {
        return this.#selector;
    }
    get id() {
        return this.#selector.id;
    }
    constructor(selectorId) {
        this.#selector = document.getElementById(selectorId);
        LangSel.all[selectorId] = this;
    }
    static elemFromId(id) {
        return Object.values(LangSel.all).find(sel => sel.id === id).elem;
    }
}

const EN = new LangSel(EN_ID);
const HU = new LangSel(HU_ID);

const PARAMS = new URLSearchParams(window.location.search);
const URL_LANG = PARAMS.get(LANG);

function setDisplay(target, value) {
    document.getElementById(MAIN_PREFIX + target).style.display = value;
}

function hideMain(lang) {
    let [on, off] = lang == EN.id ? [EN.id, HU.id] : [HU.id, EN.id];
    setDisplay(on, BLOCK);
    setDisplay(off, NONE);
    LangSel.elemFromId(on).classList.add(SEL_CLS);
    LangSel.elemFromId(off).classList.remove(SEL_CLS);
}

function getCurrentLang() {
    return localStorage.getItem(LANG) || EN.id;
}

function setParamLang(lang) {
    localStorage.setItem(LANG, lang);
    PARAMS.set(LANG, lang);
    window.history.replaceState({}, '', `${location.pathname}?${PARAMS}`);
}

function delParamLang() {
    PARAMS.delete(LANG);
    window.history.replaceState({}, '', `${location.pathname}?${PARAMS}`);
}

function chooseLanguage(lang, firstCall = false) {
    document.body.classList.remove(SBS_CLS);
    if (firstCall) {
        lang = URL_LANG || getCurrentLang();
    }
    else {
        if (getCurrentLang() == lang) return false;
    }
    setParamLang(lang);
    hideMain(lang);
    return true;
}

EN.elem.addEventListener("click", e => {
    chooseLanguage(EN.id);
});

HU.elem.addEventListener("click", e => {
    chooseLanguage(HU.id);
})

document.addEventListener("keydown", (event) => {
    if (event.altKey) {
        switch (event.key) {
            case "a":
            case "e":
                event.preventDefault();
                chooseLanguage(EN.id);
                break;
            case "h":
            case "m":
                event.preventDefault();
                chooseLanguage(HU.id);
                break;
            case "s":
                event.preventDefault();
                const cl = document.body.classList;
                if (cl.contains(SBS_CLS)) {
                    chooseLanguage(EN.id, true);
                }
                else {
                    cl.add(SBS_CLS);
                    setDisplay(EN.id, BLOCK);
                    setDisplay(HU.id, BLOCK);
                }
                break;
        }
    }
});

chooseLanguage(EN.id, true);
