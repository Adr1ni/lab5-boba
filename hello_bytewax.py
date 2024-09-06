from bytewax.dataflow import Dataflow
from bytewax.inputs import ManualInputConfig
from bytewax.outputs import StdOutputConfig
from bytewax.execution import run_main

# Configuración del flujo de datos
flow = Dataflow()
flow.input("input", ManualInputConfig(lambda: [("key", "Hola Mundo desde Bytewax!")]))
flow.output("output", StdOutputConfig())

# Ejecutar el flujo
run_main(flow)
