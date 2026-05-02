def _safe_float(value, default=0.0):
    try:
        if value is None or value == "":
            return default
        return float(value)
    except ValueError:
        return default


def _safe_int(value, default=0):
    try:
        if value is None or value == "":
            return default
        return int(value)
    except ValueError:
        return default


def _percentage(part, total):
    if total <= 0:
        return 0
    return round((part / total) * 100, 1)


def generate_mycoach_report(form):
    holes = _safe_int(form.get("holes"), 18)
    par = _safe_int(form.get("par"), 72)

    score = _safe_int(form.get("score"), par)
    fairways_hit = _safe_int(form.get("fairways_hit"), 0)
    fairways_possible = _safe_int(form.get("fairways_possible"), 14)
    greens_hit = _safe_int(form.get("greens_hit"), 0)
    putts = _safe_int(form.get("putts"), 36)
    penalties = _safe_int(form.get("penalties"), 0)
    three_putts = _safe_int(form.get("three_putts"), 0)
    up_and_downs = _safe_int(form.get("up_and_downs"), 0)
    up_and_down_chances = _safe_int(form.get("up_and_down_chances"), 0)

    driver_miss = form.get("driver_miss") or "No clear pattern"
    approach_miss = form.get("approach_miss") or "No clear pattern"
    round_notes = form.get("round_notes") or ""

    score_to_par = score - par
    fairway_pct = _percentage(fairways_hit, fairways_possible)
    gir_pct = _percentage(greens_hit, holes)
    up_down_pct = _percentage(up_and_downs, up_and_down_chances)

    strengths = []
    weaknesses = []
    practice_focus = []

    if fairway_pct >= 65:
        strengths.append("Driving accuracy was a strength. You gave yourself enough playable looks off the tee.")
    elif fairway_pct < 45:
        weaknesses.append("Driving accuracy created pressure. Too many holes likely started from recovery positions.")
        practice_focus.append("Tee shot start lines and committed targets")

    if gir_pct >= 55:
        strengths.append("Approach play was strong. Hitting greens gave you more stress-free scoring chances.")
    elif gir_pct < 40:
        weaknesses.append("Approach play was the biggest scoring leak. Missing too many greens forces the short game to save the round.")
        practice_focus.append("Approach distance control and green-target discipline")

    if putts <= 30:
        strengths.append("Putting was a clear strength. You converted well and avoided wasting strokes on the greens.")
    elif putts >= 36:
        weaknesses.append("Putting cost strokes. The round likely included too many two-putt misses or poor first-putt speed.")
        practice_focus.append("Lag putting speed control and short putt start line")

    if penalties == 0:
        strengths.append("You avoided penalty strokes, which protects the scorecard and keeps momentum stable.")
    elif penalties >= 2:
        weaknesses.append("Penalty strokes had a major impact. These are high-cost mistakes that need to be reduced first.")
        practice_focus.append("Conservative targets when trouble is in play")

    if three_putts >= 2:
        weaknesses.append("Three-putts added avoidable damage. This usually points to speed control more than stroke mechanics.")
        practice_focus.append("Long-putt speed control")

    if up_and_down_chances > 0:
        if up_down_pct >= 50:
            strengths.append("Short game recovery was solid. You saved strokes when greens were missed.")
        elif up_down_pct < 35:
            weaknesses.append("Scrambling was below target. Missed greens were turning into bogeys too often.")
            practice_focus.append("Basic chip-and-putt conversion from common misses")

    if not strengths:
        strengths.append("You completed the round with enough data to identify clear improvement priorities.")

    if not weaknesses:
        weaknesses.append("No major weakness dominated the round. The next step is improving consistency across all phases.")

    if not practice_focus:
        practice_focus.append("Balanced practice: tee shots, approach control, and putting speed")

    if score_to_par <= 0:
        round_summary = "Strong round. Your performance shows good control, limited damage, and a scoring structure that can travel."
    elif score_to_par <= 6:
        round_summary = "Competitive round. A few specific leaks kept the score from being lower, but the foundation is solid."
    elif score_to_par <= 12:
        round_summary = "Development round. The score suggests there were repeated mistakes, but the improvement path is clear."
    else:
        round_summary = "High-variance round. The priority should be reducing big mistakes before chasing aggressive scoring."

    if penalties >= 2:
        main_priority = "Course Management"
    elif gir_pct < 40:
        main_priority = "Approach Play"
    elif putts >= 36 or three_putts >= 2:
        main_priority = "Putting"
    elif fairway_pct < 45:
        main_priority = "Driving Accuracy"
    else:
        main_priority = "Consistency"

    coach_insight = (
        f"{round_summary} Your main priority from this round is {main_priority.lower()}. "
        f"The biggest pattern to watch is driver miss: {driver_miss}, and approach miss: {approach_miss}."
    )

    return {
        "score": score,
        "par": par,
        "score_to_par": score_to_par,
        "fairway_pct": fairway_pct,
        "gir_pct": gir_pct,
        "putts": putts,
        "penalties": penalties,
        "three_putts": three_putts,
        "up_down_pct": up_down_pct,
        "main_priority": main_priority,
        "round_summary": round_summary,
        "coach_insight": coach_insight,
        "strengths": strengths[:3],
        "weaknesses": weaknesses[:3],
        "practice_focus": practice_focus[:3],
        "driver_miss": driver_miss,
        "approach_miss": approach_miss,
        "round_notes": round_notes,
    }
