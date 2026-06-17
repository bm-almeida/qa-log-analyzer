from analyzer import analyze_logs

def test_log_analysis():
    sample_logs = [
        "INFO System started",
        "WARNING Low memory",
        "Error Database failed"
                 ]
    
    result = analyze_logs(sample_logs)
    assert result["INFO"] == 1
    assert result["WARNING"] == 1
    assert result["ERROR"] == 1
    