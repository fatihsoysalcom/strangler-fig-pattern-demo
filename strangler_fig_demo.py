import time

# --- Legacy System --- 
class LegacySystem:
    def process_request(self, data):
        print(f"[LEGACY] Processing request: {data}")
        # Simulate complex legacy processing
        time.sleep(0.5)
        result = f"Legacy processed: {data.upper()}"
        print(f"[LEGACY] Result: {result}")
        return result

# --- New System Component --- 
class NewFeatureA:
    def handle_request(self, data):
        print(f"[NEW A] Handling new feature A for: {data}")
        # Simulate new, faster processing
        time.sleep(0.2)
        result = f"New Feature A handled: {data.lower()}"
        print(f"[NEW A] Result: {result}")
        return result

# --- Facade / Proxy (The Strangler Fig) --- 
class StranglerFacade:
    def __init__(self, legacy_system):
        self.legacy_system = legacy_system
        self.new_feature_a = NewFeatureA() # Initialize new component
        self.routing_rules = {
            'feature_a': 'new_a', # Route 'feature_a' to the new system
            'default': 'legacy'    # Default to legacy
        }

    def process(self, request_type, data):
        route = self.routing_rules.get(request_type, self.routing_rules['default'])

        if route == 'new_a':
            # Redirect to the new system component
            return self.new_feature_a.handle_request(data)
        else: # route == 'legacy'
            # Continue using the legacy system
            return self.legacy_system.process_request(data)

# --- Simulation --- 
if __name__ == "__main__":
    print("--- Starting Strangler Fig Pattern Simulation ---")

    # 1. Initialize the legacy system
    legacy = LegacySystem()

    # 2. Introduce the facade that will eventually strangle the legacy system
    facade = StranglerFacade(legacy)

    # 3. Simulate requests
    print("\n--- First request (routed to legacy) ---")
    response1 = facade.process('normal_request', 'Hello World')
    print(f"Final response: {response1}")

    print("\n--- Second request (routed to new feature A) ---")
    response2 = facade.process('feature_a', 'New Data')
    print(f"Final response: {response2}")

    print("\n--- Third request (routed to legacy) ---")
    response3 = facade.process('another_request', 'More Data')
    print(f"Final response: {response3}")

    print("\n--- Simulation Complete ---")
    print("The facade is gradually redirecting traffic to new components.")
