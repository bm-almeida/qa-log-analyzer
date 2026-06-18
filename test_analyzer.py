from analyzer import analyze_logs
import json

def test_log_analysis():
    sample_logs = [
        "INFO System started",
        "WARNING Low memory",
        "ERROR Database failed",
        "Warning this failed connection could trigger errors",
        "error connection lost"
                 ]
    
    result = analyze_logs(sample_logs)

    print("=== DEMO OUTPUT ===")
    print(json.dumps(result, indent=4))

if __name__ == "__main__":
    test_log_analysis()    

    