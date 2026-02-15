class Policy:
    def decide(self, state):
        if not state.get("environment_scanned"):
            return "scan_environment"

        if not state.get("items_detected"):
            return "detect_items"

        if not state.get("items_sorted"):
            return "sort_items"

        if not state.get("items_packed"):
            return "pack_items"

        return "complete_task"
