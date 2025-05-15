from datetime import datetime as dt

from pyscript import document
from pyweb import pydom

tasks = []

def q(selector, root=document):
    return root.querySelector(selector)

meta_template = """\
<h1 id="message" onclick="copyDivToClipboard()"> Copy to Clipboard </h1>
<div id="greenmetayml">
travel: TBD # TBD
experimental-work: TBD # TBD
computing:
    embodied: # TBD
        carbon-footprint: TBD # TBD
        abiotic-resource-depletion:  TBD # TBD
    operational:
        impact-values:
            energy-consumption: %(energy_consumption)s # kWh - float
            carbon-footprint: %(carbon_footprint)s     # gCO2e - float
            water-consumption:  %(water_consumption)s  # liters - float
        methods-and-scope:
            software-boundaries:  TBD # TBD
            hardware-boundaries: 
                components-used:  # TBD
                infrastructure:
                    power-usage-efficiency:
                        PUE: %(pue)s # float
                        estimation-method: %(pue_estimation_method)s # text
                    water-usage-effectiveness:
                        value: %(water_usage_effectiveness)s # L/kWh
                        estimation-method: %(wue_estimation_method)s # text
                electricity-carbon-intensity:
                    value: %(eci_value)s gCO2/kWh # Float
                    source: %(eci_source)s # text
</div>
"""

meta_container = pydom["#meta-container"][0]

meta_1 = pydom["#meta-1"][0]
meta_2 = pydom["#meta-2"][0]
meta_3 = pydom["#meta-3"][0]
meta_4 = pydom["#meta-4"][0]
meta_5 = pydom["#meta-5"][0]
meta_6 = pydom["#meta-6"][0]
meta_7 = pydom["#meta-7"][0]
meta_8 = pydom["#meta-8"][0]
meta_9 = pydom["#meta-9"][0]

def add_meta(e):
    first = meta_1.value
    second = meta_2.value
    third = meta_3.value

    values = {
        "energy_consumption" : meta_1.value,
        "carbon_footprint" : meta_2.value,
        "water_consumption" : meta_3.value,
        "pue" : meta_4.value,
        "pue_estimation_method" : meta_5.value,
        "water_usage_effectiveness" :  meta_6.value,
        "wue_estimation_method" : meta_7.value,
        "eci_value" : meta_8.value,
        "eci_source" : meta_9.value
    }

    meta_html = meta_template % values
    meta_container.html = meta_html
