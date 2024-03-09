#!/usr/bin/env python3
"""Generate forms for human evaluation."""
from pathlib import Path

from jinja2 import FileSystemLoader, Environment
import json

def main():
    """Main function."""
    loader = FileSystemLoader(searchpath="./templates")
    env = Environment(loader=loader)
    template = env.get_template("mos.html.jinja2")

    with open("samples_gt/samples.json", 'r') as f:
        samples_json = json.load(f)

    directories = [
        'gt',
        'mms',
        'roboshaul',
        'word_osim',
        'word_shaul'
    ]

    # questions = [
    #     {
    #         "id": i,
    #         "prompt": s['prompt'],
    #         "recordings": [
    #             {
    #                 'title': d,
    #                 'audio_path': f"samples/{d}/{s['index']}.wav",
    #                 'name': f"{d}_{s['index']}"
    #             } for d in directories
    #         ]
    #     } for i, s in enumerate(samples_json)
    # ]

    questions = [
        {
            'dir': d,
            'prompt': s['prompt'],
            'title': f"dir {d}, index {s['index']}",
            'audio_path': f"samples_gt/{d}/{s['index']}.wav",
            'name': f"{d}_{s['index']}"
        } for d in directories for i, s in enumerate(samples_json)
    ]

    # additional samples
    questions += [
        {
            'dir': 'additional',
            'prompt': "תגידו גנבו לכם פעם את האוטו ופשוט ידעתם שאין טעם להגיש תלונה במשטרה?",
            'title': f"word_osim_add_1",
            'audio_path': f"samples/word_osim/2.wav",
            'name': f"word_osim_additional_1"
        },
        {
            'dir': 'additional',
            'prompt': "בראשית היתה חללית מסוג נחתת",
            'title': f"word_osim_add_2",
            'audio_path': f"samples/word_osim/6.wav",
            'name': f"word_osim_additional_2"
        },
        {
            'dir': 'additional',
            'prompt': "הדרבי תמיד היה המשחק הכי חשוב, אך בשני האחרונות הוא נעשה כמעט הדבר היחיד שחשוב",
            'title': f"word_osim_add_3",
            'audio_path': f"samples/word_osim/4.wav",
            'name': f"word_osim_additional_3"
        },
        {
            'dir': 'additional',
            'prompt': "ובשביל להבין למה מחיר הדלק כל כך עלה, צריך לחזור שנתיים אחרונית",
            'title': f"word_osim_add_4",
            'audio_path': f"samples/word_osim/1.wav",
            'name': f"word_osim_additional_4"
        },

        {
            'dir': 'additional',
            'prompt': "מה שבהגדרה משאיר את הכלכלה ההונגרית מאחור, אפילו ביחס למדינות כמו פולין",
            'title': f"word_shaul_add_1",
            'audio_path': f"samples/word_roboshaul/3.wav",
            'name': f"word_shaul_additional_1"
        },
    ]

    html = template.render(
        page_title="MOS",
        form_url="https://script.google.com/macros/s/AKfycbybOLJ5rGWHwhLSF21H4E1KRHKQJ5R1yo3XSdnWhqhCnvPgKdLBHr5zeNifqtkhb2Nwtg/exec",
        form_id=1,
        questions=questions
    )

    with open("rendered_mos.html", 'w') as f:
        f.write(html)

    print(html)

    print(html)


if __name__ == "__main__":
    main()
