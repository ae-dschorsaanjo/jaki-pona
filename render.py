#! /usr/bin/env python3


from markdown import markdown
from re import sub


def read_file(path: str, is_markdown: bool = False) -> str:
    with open(path, 'r', encoding='utf-8') as f:
        if is_markdown:
            text = f.read()
            text = sub(r"> *(.*[^ ]) *\| *(.*[^ \n])\n?",
                       f'> <div class="block-left">\\1</div><div class="block-right">(\\2)</div>\n', text)
            return text
        return f.read()


def render_markdown(text):
    return markdown(text,
                    extensions=['attr_list', 'def_list', 'smarty',
                                'tables'],
                    extension_configs={
                        'smarty': {'smart_dashes': True,
                                   'smart_quotes': False,
                                   'smart_ellipses': True}})


def render(main_en: str, main_hu: str,
           dict_en: str, dict_hu: str,
           css_fonts: str, css_global: str, css_default: str,
           css_print: str, js_lang: str, template: str):
    main_en = render_markdown(read_file(main_en, True))
    main_hu = render_markdown(read_file(main_hu, True))
    dict_en = render_markdown(read_file(dict_en, True))
    # dict_hu = render_markdown(read_file(dict_hu, True))
    # FIXME: remove override
    dict_hu = ''
    css_fonts = read_file(css_fonts)
    css_global = read_file(css_global)
    css_default = read_file(css_default)
    css_print = read_file(css_print)
    js_lang = read_file(js_lang)
    template = read_file(template)
    out = template.format(CSS_FONTS=css_fonts,
                          CSS_GLOBAL=css_global,
                          CSS_DEFAULT=css_default,
                          CSS_PRINT=css_print,
                          JS_LANG=js_lang,
                          MAIN_EN=main_en,
                          MAIN_HU=main_hu,
                          DICT_EN=dict_en,
                          DICT_HU=dict_hu)
    with open('docs/index.html', 'w', encoding='utf-8') as f:
        f.write(out)
    return len(out)


if __name__ == '__main__':
    print(render('jaki_pona-en.md', 'jaki_pona-hu.md',
                 'dict_en.md', 'dict_hu.md',
                 'res/fonts.css', 'res/global.css',
                 'res/default.css', 'res/print.css',
                 'res/langsel.js', 'res/template.html'))
