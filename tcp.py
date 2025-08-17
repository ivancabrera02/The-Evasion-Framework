import time
import json
import etw
import argparse
import os

def main(pid_filter):
    # GUID del proveedor Microsoft-Windows-Kernel-Network
    provider_guid = etw.GUID("{7DD42A49-5329-4832-8DFD-43D979153A88}")

    def consumer(event):
        event_json = json.dumps(event)
        event_data = json.loads(event_json)

        # Filtrar por PID
        pid = event_data[1].get("PID", None)
        if pid != pid_filter:
            return  # Ignorar eventos de otros procesos

        task_name = event_data[1].get("Task Name", "")
        if "TCP" in task_name or "UDP" in task_name:
            print(f"Evento: {task_name}")
            print(json.dumps(event_data[1], indent=2))
            print("-" * 40)

            with open("network_events.jsonl", "a") as f:
                json.dump(event_data[1], f)
                f.write("\n")

    # Crear la sesión ETW para el proveedor de red
    session = etw.ETW(
        providers=[etw.ProviderInfo("Microsoft-Windows-Kernel-Network", provider_guid)],
        session_name="Network-Monitor-Session",
        event_callback=consumer
    )

    print(f"[*] Iniciando sesión ETW para conexiones de red del PID {pid_filter}. Ctrl+C para parar.")
    session.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("[*] Deteniendo sesión ETW.")
        session.stop()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Monitor ETW de conexiones de red para un PID específico.")
    parser.add_argument("--pid", required=True, type=int, help="PID del proceso a monitorizar.")
    args = parser.parse_args()

    main(args.pid)

