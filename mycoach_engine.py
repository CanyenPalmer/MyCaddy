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


PGA_REFERENCES = {
    "fairways": {
        "label": "Fairways Hit",
        "unit": "%",
        "top_10": 70,
        "top_50": 65,
        "tour_average": 60,
        "higher_is_better": True,
    },
    "gir": {
        "label": "Greens in Regulation",
        "unit": "%",
        "top_10": 70,
        "top_50": 65,
        "tour_average": 60,
        "higher_is_better": True,
    },
    "putts": {
        "label": "Putts Per Round",
        "unit": "",
        "top_10": 28,
        "top_50": 29,
        "tour_average": 30,
        "higher_is_better": False,
    },
    "scrambling": {
        "label": "Scrambling",
        "unit": "%",
        "top_10": 65,
        "top_50": 60,
        "tour_average": 55,
        "higher_is_better": True,
    },
    "penalties": {
        "label": "Penalty Strokes",
        "unit": "",
        "top_10": 0,
        "top_50": 1,
        "tour_average": 1,
        "higher_is_better": False,
    },
}


DRILLS = {
    "Tee Box Accuracy": {
        "name": "Fairway Finder Start-Line Drill",
        "setup": "On the range, pick a fairway-width target window. Place two alignment sticks or clubs on the ground to create a start-line gate just a few yards in front of the ball.",
        "execution": "Hit 10 tee shots using the club you normally trust from the tee. Your only goal is to start the ball through the gate and finish inside the target window. Track how many out of 10 would be playable.",
        "goal": "Finish 7 out of 10 balls inside the target window before increasing speed or changing clubs.",
        "helps": "Tee shot commitment, start-line control, and choosing a reliable club when accuracy matters.",
    },
    "Approach Play": {
        "name": "Green-Center Approach Drill",
        "setup": "Pick three approach distances. Instead of aiming at pins, choose the center of the green or the safest section of the target.",
        "execution": "Hit 5 balls from each distance. Score each ball as green hit, safe miss, or short-side/big miss. The goal is to remove high-cost misses, not chase perfect shots.",
        "goal": "Hit or safely miss 10 out of 15 shots before moving to harder targets.",
        "helps": "Approach discipline, distance control, and smarter target selection.",
    },
    "Approach Distance Control": {
        "name": "Distance Ladder Approach Drill",
        "setup": "Choose three yardages that commonly appear in your rounds. Use alignment and a clear landing target for each number.",
        "execution": "Hit 3 balls to the short number, 3 to the middle number, and 3 to the long number. Repeat the ladder twice. Track whether each ball finishes pin-high, short, or long.",
        "goal": "Get at least 6 out of 9 balls finishing within a playable distance window.",
        "helps": "Carry control, club selection, and reducing short/long approach misses.",
    },
    "Putting Speed": {
        "name": "Ladder Speed Control Drill",
        "setup": "Place tees or ball markers at 20, 30, and 40 feet from a hole or target zone.",
        "execution": "Roll 3 putts from each distance. The goal is to finish every putt inside a 3-foot circle around the hole, not necessarily make it.",
        "goal": "Get 7 out of 9 putts inside the 3-foot circle.",
        "helps": "Lag putting, three-putt avoidance, and distance control on the greens.",
    },
    "Putting Start Line": {
        "name": "Gate Putting Drill",
        "setup": "Place two tees just wider than your putter head about 12 inches in front of the ball on a straight 4-to-6-foot putt.",
        "execution": "Roll putts through the gate without touching either tee. Start close enough to build confidence, then increase the distance.",
        "goal": "Make 10 putts in a row through the gate before moving farther away.",
        "helps": "Face control, start line, and short-putt confidence.",
    },
    "Putting Green Reading": {
        "name": "Around-the-Clock Read Drill",
        "setup": "Place balls around one hole at 3 to 6 feet from multiple angles: uphill, downhill, left-to-right, and right-to-left.",
        "execution": "Before each putt, call the break and speed out loud. Then putt and compare the actual result to your read.",
        "goal": "Correctly match read and speed on at least 6 out of 8 putts.",
        "helps": "Green reading, speed matching, and confidence on breaking putts.",
    },
    "Short Game": {
        "name": "Up-and-Down Challenge",
        "setup": "Pick 9 short-game spots around a practice green: easy, medium, and difficult lies.",
        "execution": "Play one ball from each spot and finish the hole. Track whether you get up and down. Use your normal pre-shot routine on every attempt.",
        "goal": "Get up and down at least 4 out of 9 times, then work toward 5 or 6.",
        "helps": "Chipping execution, recovery scoring, and converting missed greens into pars.",
    },
    "Penalties": {
        "name": "Trouble Avoidance Target Drill",
        "setup": "On the range or course, choose targets with an imaginary hazard or out-of-bounds side.",
        "execution": "For each shot, pick a target that removes the big miss. Hit 10 balls and score each as safe, playable miss, or penalty miss.",
        "goal": "Complete 10 shots with zero penalty-side misses.",
        "helps": "Course management, conservative target selection, and avoiding scorecard-damaging mistakes.",
    },
    "Course Management": {
        "name": "Smart Bogey Drill",
        "setup": "Play or simulate holes where trouble is in play. Before each shot, choose the option that guarantees the next shot is playable.",
        "execution": "Your goal is to avoid doubles or worse. When out of position, practice returning to safety instead of forcing a heroic recovery.",
        "goal": "Complete 6 trouble scenarios without making a double-bogey decision.",
        "helps": "Damage control, decision-making, and smarter scoring under pressure.",
    },
    "Pressure": {
        "name": "3-6-9 Pressure Putting Drill",
        "setup": "Place one ball at 3 feet, one at 6 feet, and one at 9 feet on the same line.",
        "execution": "Make the 3-footer, then the 6-footer, then the 9-footer. If you miss, restart from 3 feet.",
        "goal": "Complete the full 3-6-9 sequence three times.",
        "helps": "Pressure conversion, routine discipline, and finishing under consequence.",
    },
    "Slow Start": {
        "name": "First-Three-Holes Warmup Simulation",
        "setup": "Before a round or practice session, simulate your first three tee shots and first three approach shots.",
        "execution": "Go through your full routine. Pick conservative targets and focus on solid contact over aggression.",
        "goal": "Start practice with 6 committed swings and no careless decisions.",
        "helps": "Starting rhythm, early-round focus, and avoiding preventable opening mistakes.",
    },
    "Poor Finish": {
        "name": "Closing Stretch Pressure Drill",
        "setup": "Create a 6-shot finish: 2 tee shots, 2 approach shots, and 2 pressure putts.",
        "execution": "Treat each shot like the final three holes of a good round. If you lose focus or rush, restart the sequence.",
        "goal": "Complete all 6 shots with full routine and committed targets.",
        "helps": "Late-round focus, closing discipline, and maintaining decision quality when tired.",
    },
    "Club Selection": {
        "name": "One-More-Club Discipline Drill",
        "setup": "Pick approach targets where a front miss is costly. Choose the club that reaches the middle or back half of the target.",
        "execution": "Hit 10 shots focusing on smooth tempo instead of forcing a shorter club. Track how often you finish pin-high or safely long.",
        "goal": "Get 7 out of 10 shots past the front edge without a big miss.",
        "helps": "Club selection, distance honesty, and reducing short misses.",
    },
}


def _score_round_tier(score_to_par):
    if score_to_par <= -3:
        return {
            "name": "Tour-Level Scoring Range",
            "description": "This is an elite scoring round. One round does not equal a PGA Tour scoring average, but the score itself is in a range that reflects extremely high-level execution.",
        }
    if score_to_par <= 0:
        return {
            "name": "Elite Amateur Round",
            "description": "This is a strong scoring round. The goal now is identifying which parts of the game are repeatable and which areas still separate the round from Tour-level consistency.",
        }
    if score_to_par <= 6:
        return {
            "name": "Competitive Round",
            "description": "This is a competitive amateur round. A few specific leaks likely kept the score from moving into a stronger scoring range.",
        }
    if score_to_par <= 12:
        return {
            "name": "Development Round",
            "description": "This round gives clear improvement signals. The focus should be reducing repeated mistakes and turning common bogeys into pars.",
        }
    return {
        "name": "High-Variance Round",
        "description": "This round had too many scoring leaks. The first goal should be reducing big numbers before chasing aggressive scoring.",
    }


def _compare_to_pga(value, reference_key):
    ref = PGA_REFERENCES[reference_key]
    top_10 = ref["top_10"]
    top_50 = ref["top_50"]
    tour_average = ref["tour_average"]

    if ref["higher_is_better"]:
        if value >= top_10:
            status = "At or above the elite PGA reference."
        elif value >= top_50:
            status = "Near a strong PGA reference."
        elif value >= tour_average:
            status = "Near the PGA Tour average reference."
        else:
            status = "Below the PGA reference range."
    else:
        if value <= top_10:
            status = "At or above the elite PGA reference."
        elif value <= top_50:
            status = "Near a strong PGA reference."
        elif value <= tour_average:
            status = "Near the PGA Tour average reference."
        else:
            status = "Below the PGA reference range."

    unit = ref["unit"]

    return {
        "label": ref["label"],
        "player_value": f"{value}{unit}" if unit else str(value),
        "top_10": f"{top_10}{unit}" if unit else str(top_10),
        "top_50": f"{top_50}{unit}" if unit else str(top_50),
        "tour_average": f"{tour_average}{unit}" if unit else str(tour_average),
        "status": status,
    }


def _add_unique(items, item):
    if item not in items:
        items.append(item)


def _build_focus_scores(
    fairway_pct,
    gir_pct,
    putts,
    penalties,
    three_putts,
    up_down_pct,
    up_and_down_chances,
    tee_box_miss,
    approach_miss,
    round_issue,
):
    focus_scores = {
        "Tee Box Accuracy": 0,
        "Approach Play": 0,
        "Short Game": 0,
        "Putting": 0,
        "Course Management": 0,
    }

    if fairway_pct < 45:
        focus_scores["Tee Box Accuracy"] += 3
    elif fairway_pct < 60:
        focus_scores["Tee Box Accuracy"] += 1

    if tee_box_miss not in ["No Issues", ""]:
        focus_scores["Tee Box Accuracy"] += 2

    if gir_pct < 40:
        focus_scores["Approach Play"] += 3
    elif gir_pct < 60:
        focus_scores["Approach Play"] += 1

    if approach_miss not in ["No Issues", ""]:
        focus_scores["Approach Play"] += 2

    if putts >= 36:
        focus_scores["Putting"] += 3
    elif putts >= 33:
        focus_scores["Putting"] += 1

    if three_putts >= 2:
        focus_scores["Putting"] += 2

    if up_and_down_chances > 0 and up_down_pct < 35:
        focus_scores["Short Game"] += 3
    elif up_and_down_chances > 0 and up_down_pct < 50:
        focus_scores["Short Game"] += 1

    if penalties >= 2:
        focus_scores["Course Management"] += 3
    elif penalties == 1:
        focus_scores["Course Management"] += 1

    issue_map = {
        "Poor Tee Shot Accuracy": "Tee Box Accuracy",
        "Poor Approach Distance Control": "Approach Play",
        "Poor Approach Accuracy": "Approach Play",
        "Poor Short Game - Chipping": "Short Game",
        "Poor Short Game - Putting": "Putting",
        "Poor Short Game - Both": "Short Game",
        "Poor Putting Speed": "Putting",
        "Poor Putting Start Line": "Putting",
        "Poor Putting Green Reading": "Putting",
        "Too Many Penalties": "Course Management",
        "Bad Club Selection": "Course Management",
        "Poor Course Management": "Course Management",
        "Struggled Under Pressure": "Course Management",
        "Slow Start": "Course Management",
        "Poor Finish": "Course Management",
    }

    if round_issue in issue_map:
        focus_scores[issue_map[round_issue]] += 2

    if round_issue == "Poor Short Game - Both":
        focus_scores["Putting"] += 2

    return focus_scores


def _primary_focus_from_scores(focus_scores):
    highest_score = max(focus_scores.values())

    if highest_score <= 0:
        return ["Consistency"]

    top_focuses = [
        focus for focus, score in focus_scores.items()
        if score == highest_score
    ]

    if "Short Game" in top_focuses and "Putting" in top_focuses:
        return ["Short Game"]

    return top_focuses[:2]


def _build_practice_plan(primary_focuses, round_issue):
    drill_keys = []

    for focus in primary_focuses:
        if focus == "Tee Box Accuracy":
            drill_keys.append("Tee Box Accuracy")
        elif focus == "Approach Play":
            if round_issue == "Poor Approach Distance Control":
                drill_keys.append("Approach Distance Control")
            else:
                drill_keys.append("Approach Play")
        elif focus == "Putting":
            if round_issue == "Poor Putting Speed":
                drill_keys.append("Putting Speed")
            elif round_issue == "Poor Putting Start Line":
                drill_keys.append("Putting Start Line")
            elif round_issue == "Poor Putting Green Reading":
                drill_keys.append("Putting Green Reading")
            else:
                drill_keys.append("Putting Speed")
        elif focus == "Short Game":
            drill_keys.append("Short Game")
        elif focus == "Course Management":
            if round_issue == "Too Many Penalties":
                drill_keys.append("Penalties")
            elif round_issue == "Bad Club Selection":
                drill_keys.append("Club Selection")
            elif round_issue == "Struggled Under Pressure":
                drill_keys.append("Pressure")
            elif round_issue == "Slow Start":
                drill_keys.append("Slow Start")
            elif round_issue == "Poor Finish":
                drill_keys.append("Poor Finish")
            else:
                drill_keys.append("Course Management")

    if not drill_keys:
        drill_keys.append("Approach Play")

    drills = []
    for key in drill_keys:
        if key in DRILLS and DRILLS[key] not in drills:
            drills.append(DRILLS[key])

    return drills[:2]


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

    tee_box_miss = form.get("tee_box_miss") or "No Issues"
    approach_miss = form.get("approach_miss") or "No Issues"
    round_issue = form.get("round_issue") or "No Major Issues"

    score_to_par = score - par
    fairway_pct = _percentage(fairways_hit, fairways_possible)
    gir_pct = _percentage(greens_hit, holes)
    up_down_pct = _percentage(up_and_downs, up_and_down_chances)

    round_tier = _score_round_tier(score_to_par)

    pga_comparisons = [
        _compare_to_pga(fairway_pct, "fairways"),
        _compare_to_pga(gir_pct, "gir"),
        _compare_to_pga(putts, "putts"),
        _compare_to_pga(up_down_pct, "scrambling"),
        _compare_to_pga(penalties, "penalties"),
    ]

    strengths = []
    weaknesses = []

    if fairway_pct >= 60:
        _add_unique(strengths, "Tee box accuracy was a strength. You put yourself in enough playable positions to keep the round organized.")
    elif fairway_pct < 45:
        _add_unique(weaknesses, "Tee box accuracy created pressure. Too many holes likely started from recovery positions.")

    if gir_pct >= 60:
        _add_unique(strengths, "Approach play compared well against a strong reference point. Hitting greens keeps stress off the short game.")
    elif gir_pct < 40:
        _add_unique(weaknesses, "Approach play was a major scoring leak. Missing greens at this rate forces the short game to carry too much of the round.")

    if putts <= 30:
        _add_unique(strengths, "Putting volume was strong. A putt total in this range usually means you avoided giving away strokes on the greens.")
    elif putts >= 36:
        _add_unique(weaknesses, "Putting cost strokes. This usually points to poor speed control, missed short putts, or too many long second putts.")

    if penalties == 0:
        _add_unique(strengths, "You avoided penalty strokes, which protects the scorecard and keeps momentum stable.")
    elif penalties >= 2:
        _add_unique(weaknesses, "Penalty strokes had a major impact. These are high-cost mistakes that should be reduced before chasing aggressive scoring.")

    if three_putts >= 2:
        _add_unique(weaknesses, "Three-putts added avoidable damage. Most three-putt problems begin with speed control, not the second putt.")

    if up_and_down_chances > 0:
        if up_down_pct >= 55:
            _add_unique(strengths, "Scrambling was a strength. You turned missed greens into saves at a strong rate.")
        elif up_down_pct < 35:
            _add_unique(weaknesses, "Scrambling was below target. Missed greens were turning into bogeys too often.")

    if tee_box_miss not in ["No Issues", ""]:
        _add_unique(weaknesses, f"Your main tee box miss was {tee_box_miss.lower()}. That pattern should guide your next tee-shot practice session.")

    if approach_miss not in ["No Issues", ""]:
        _add_unique(weaknesses, f"Your main approach miss was {approach_miss.lower()}. That pattern matters because approach play is one of the biggest scoring separators.")

    if round_issue != "No Major Issues":
        _add_unique(weaknesses, f"You identified {round_issue.lower()} as a round trend. That self-scouting input should influence the practice plan.")

    if not strengths:
        strengths.append("You completed the round with enough detail to identify clear improvement priorities. That alone makes the next practice session more targeted.")

    if not weaknesses:
        weaknesses.append("No major weakness dominated the round. The next step is building repeatability and comparing your best patterns against stronger scoring benchmarks.")

    focus_scores = _build_focus_scores(
        fairway_pct,
        gir_pct,
        putts,
        penalties,
        three_putts,
        up_down_pct,
        up_and_down_chances,
        tee_box_miss,
        approach_miss,
        round_issue,
    )

    primary_focuses = _primary_focus_from_scores(focus_scores)

    practice_plan = _build_practice_plan(primary_focuses, round_issue)

    if len(primary_focuses) == 1:
        focus_text = primary_focuses[0]
    else:
        focus_text = " + ".join(primary_focuses)

    miss_sentences = []

    if tee_box_miss not in ["No Issues", ""]:
        miss_sentences.append(f"Your tee box miss pattern was {tee_box_miss.lower()}.")

    if approach_miss not in ["No Issues", ""]:
        miss_sentences.append(f"Your approach miss pattern was {approach_miss.lower()}.")

    if round_issue != "No Major Issues":
        miss_sentences.append(f"The round trend you identified was {round_issue.lower()}.")

    if miss_sentences:
        pattern_text = " ".join(miss_sentences)
    else:
        pattern_text = "There was no major miss pattern selected, so the report is driven primarily by your scoring statistics."

    coach_insight = (
        f"{round_tier['description']} Your primary focus is {focus_text.lower()}. "
        f"{pattern_text} The practice plan below is built to attack the clearest scoring leak from this round."
    )

    return {
        "score": score,
        "par": par,
        "score_to_par": score_to_par,
        "holes": holes,
        "fairway_pct": fairway_pct,
        "gir_pct": gir_pct,
        "putts": putts,
        "penalties": penalties,
        "three_putts": three_putts,
        "up_down_pct": up_down_pct,
        "primary_focuses": primary_focuses,
        "focus_text": focus_text,
        "round_tier": round_tier,
        "coach_insight": coach_insight,
        "strengths": strengths[:4],
        "weaknesses": weaknesses[:4],
        "practice_plan": practice_plan,
        "tee_box_miss": tee_box_miss,
        "approach_miss": approach_miss,
        "round_issue": round_issue,
        "pga_comparisons": pga_comparisons,
    }
