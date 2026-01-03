const EN_ID = "en";
const HU_ID = "hu";
const SEL_CLS = "sel";
const MAIN_PREFIX = "main-";
const LANG = "lang";
const SBS_CLS = "sbs";

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
        return LangSel.selFromId(id).elem;
    }
    static idFromId(id) {
        return LangSel.selFromId(id).id;
    }
    static selFromId(id) {
        return Object.values(LangSel.all).find(sel => sel.id == id);
    }
}

const EN = new LangSel(EN_ID);
const HU = new LangSel(HU_ID);

function setDisplay(target, value) {
    document.getElementById(MAIN_PREFIX + target).style.display = value;
}

function hideMain(lang) {
    let [on, off] = lang == EN.id ? [EN.id, HU.id] : [HU.id, EN.id];
    setDisplay(on, 'block');
    setDisplay(off, 'none');
    LangSel.elemFromId(on).classList.add(SEL_CLS);
    LangSel.elemFromId(off).classList.remove(SEL_CLS);
}

function getCurrentLang() {
    return localStorage.getItem(LANG) || EN.id;
}

function chooseLanguage(lang, first_call = false) {
    document.body.classList.remove(SBS_CLS);
    
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
                    setDisplay(EN.id, "block");
                    setDisplay(HU.id, "block");
                }
                break;
        }
    }
});

chooseLanguage(EN.id, true);

// TODO: update URL based on language selection and be able to
//       read selected language from URL