import time

print("🚀 Started")

try:
    while True:
        print("Hello World")
        time.sleep(5)

except KeyboardInterrupt:
    print("\n🛑 Shutdown requested. Exiting gracefully...")
