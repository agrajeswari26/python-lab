import json

data= [
    {
        "timestamp": "10:00",
        "level": "INFO",
        "message": "Application started"
    },
    {
        "timestamp": "10:05",
        "level": "WARNING",
        "message": "Low memory"
    },
    {
        "timestamp": "10:10",
        "level": "ERROR",
        "message": "Database connection failed"
    }
]

# Write initial data to logs.json for testing
with open("logs.json", "w") as f:
    json.dump(data, f, indent=4)

def analyze_logs(filename="logs.json"):
    try:
        # 1. Read the JSON file
        with open(filename, "r") as file:
            logs = json.load(file)
            
        info_count = 0
        warning_count = 0
        error_count = 0
        
        # 2. Display all log records
        print("--- All Log Records ---")
        for log in logs:
            print(f"[{log.get('timestamp')}] {log.get('level')}: {log.get('message')}")
            
            # 3. Count messages by category
            level = log.get('level')
            if level == "INFO":
                info_count += 1
            elif level == "WARNING":
                warning_count += 1
            elif level == "ERROR":
                error_count += 1

        # 4. Display the summary
        print("\n--- Log Summary ---")
        print(f"INFO messages: {info_count}")
        print(f"WARNING messages: {warning_count}")
        print(f"ERROR messages: {error_count}")
        
    # 5. Handle missing files and invalid JSON data
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except json.JSONDecodeError:
        print(f"Error: '{filename}' contains invalid JSON data.")
    except Exception as e:
         print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    analyze_logs()
