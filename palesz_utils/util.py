from flask import (
    Blueprint, flash, render_template, request
)

import textwrap

bp = Blueprint('util', __name__)

# werkzeug - szerszam

# Use single-quotes for string literals, e.g. 'my-identifier' , but use double-quotes for strings that are likely to contain single-quote characters as part of the string itself


@bp.route('/dilution', methods=('GET', 'POST'))
def dilution() -> str:
    if request.method == 'POST':
        try:
            volume: float = float(request.form['volume'])
            act_alcohol_level: float = float(request.form['act_alcohol_level'])
            target_alcohol_level: float = float(request.form['target_alcohol_level'])

            assert volume > 0, 'A liter pozitív kell legyen!'
            assert act_alcohol_level > 0, 'A mostani alkoholszint pozitív kell legyen!'
            assert target_alcohol_level > 0, 'Az elérni kívánt alkoholszint pozitív kell legyen!'
            assert 100 >= act_alcohol_level, 'Na azt hogy csináltad, h 100%-nál nagyobb az alkoholszint?!'
            assert target_alcohol_level < act_alcohol_level, \
                'Az elérni kívánt alkoholszint kisebb kell legyen, mint a mostani!'

            output_value: float = (volume * act_alcohol_level / target_alcohol_level) - volume
            output: str = (f"({volume:.2f}L * {act_alcohol_level:.2f}% / {target_alcohol_level:.2f}%) - {volume:.2f}L "
                           f"== {output_value:.2f} Liter vízre van szükség")

            return render_template('util/dilution.html', output=output)
        except Exception as e:
            flash(str(e))
    return render_template('util/dilution.html')


@bp.route('/separation', methods=('GET', 'POST'))
def partitioning() -> str:
    if request.method == 'POST':
        try:
            volume: float = float(request.form['volume'])

            assert volume > 0, 'A liter pozitív kell legyen!'

            full_head_min: float = volume * 0.05
            full_head_max: float = volume * 0.2
            copper_part_min: float = volume * 0.03
            copper_part_max: float = volume * 0.05
            head_min: float = volume * 0.05
            head_max: float = volume * 0.15

            output: str = textwrap.dedent(f"""\
            Az előpárlat várható teljes mennyisége: {full_head_min:.2f} dL - {full_head_max:.2f} dL
            
            Ebből a rézeleje (mindenképp kuka): {copper_part_min:.2f} dL - {copper_part_max:.2f} dL
            Az rézeleje után nyert előpárlat, amit poharazni lehet:  {head_min:.2f} dL - {head_max:.2f} dL""")

            return render_template('util/separation.html', output=output)
        except Exception as e:
            flash(str(e))
            return render_template('util/separation.html')

    return render_template('util/separation.html')
