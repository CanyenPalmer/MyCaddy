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
    "Tee Box Right Miss": {
        "name": "Tee Shot Start-Line Gate Drill",
        "setup": "On the range, choose a fairway-width target. Place two alignment sticks or clubs on the ground to create a start-line gate a few yards in front of the ball.",
        "execution": "Hit 10 tee shots using the club you normally trust off the tee. Your only goal is to start the ball through the gate and finish inside the target window.",
        "goal": "Get 7 out of 10 tee shots starting through the gate and finishing playable.",
        "helps": "Right misses, open-face delivery, poor start line, and tee-shot commitment.",
    },
    "Tee Box Left Miss": {
        "name": "Hold-Off Tee Shot Drill",
        "setup": "Pick a target and create a start-line gate slightly right of the target if you tend to miss left.",
        "execution": "Hit controlled tee shots at 75 percent speed while feeling the clubface stay stable through impact. Do not chase distance during this drill.",
        "goal": "Hit 7 out of 10 tee shots without the ball starting or curving hard left.",
        "helps": "Left misses, over-release patterns, and tee shots that turn over too aggressively.",
    },
    "Tee Box Penalty Trouble": {
        "name": "Trouble-Side Avoidance Drill",
        "setup": "Pick a range target and define one side as penalty trouble. Choose a target line that removes that side from play.",
        "execution": "Hit 10 tee shots. Score each shot as safe, playable miss, or penalty-side miss.",
        "goal": "Complete 10 tee shots with zero penalty-side misses.",
        "helps": "Penalty avoidance, conservative target selection, and smarter tee-box decisions.",
    },
    "Tee Box Inconsistent": {
        "name": "Fairway Finder Drill",
        "setup": "Choose your most reliable tee club. Pick a narrow but realistic target window.",
        "execution": "Hit 10 balls using a shorter, controlled finish. Track only whether each ball would be playable from the tee.",
        "goal": "Get 7 out of 10 balls into a playable position before increasing speed.",
        "helps": "Tee-box consistency, tempo, and building a reliable fairway-finder shot.",
    },
    "Tee Box Bad Swing": {
        "name": "Tempo Tee Shot Ladder",
        "setup": "Use your normal tee club and pick a wide target. Prepare to hit three speed levels: 60 percent, 75 percent, and 90 percent.",
        "execution": "Hit 3 balls at each speed. Only move up if contact and balance are stable. If contact breaks down, return to the previous speed.",
        "goal": "Finish the ladder with balanced contact on at least 7 out of 9 swings.",
        "helps": "Bad swing patterns, rushed tempo, and tee shots where mechanics break under speed.",
    },
    "Tee Box Short": {
        "name": "Efficient Contact Tee Drill",
        "setup": "Tee the ball at your normal height and place a small towel several inches behind the ball.",
        "execution": "Hit tee shots without striking the towel. Focus on centered contact and a balanced finish, not swinging harder.",
        "goal": "Hit 8 out of 10 tee shots with clean contact and balanced finish.",
        "helps": "Short tee shots caused by poor contact, steep delivery, or inefficient strike.",
    },
    "Tee Box Long": {
        "name": "Controlled Target Tee Drill",
        "setup": "Choose a target where going long creates trouble. Use one less club or a smoother tee swing.",
        "execution": "Hit 10 tee shots trying to finish short of the trouble while staying in play.",
        "goal": "Keep 8 out of 10 shots short of the long-side trouble and playable.",
        "helps": "Over-aggressive tee shots, long misses, and better club selection from the tee.",
    },
    "Approach Short": {
        "name": "One-More-Club Approach Drill",
        "setup": "Pick approach targets where a front miss would be costly. Choose the club that reaches the middle or back half of the target.",
        "execution": "Hit 10 approach shots with smooth tempo. Track whether each shot finishes short, pin-high, or safely past the front edge.",
        "goal": "Get 7 out of 10 shots past the front edge without creating a big miss.",
        "helps": "Short approach misses, club selection honesty, and distance control.",
    },
    "Approach Long": {
        "name": "Back-Edge Control Drill",
        "setup": "Pick a green or target zone and define a clear back edge that the ball must not pass.",
        "execution": "Hit 10 approach shots while choosing clubs and targets that keep the ball under control. Score each shot as safe, long, or big miss.",
        "goal": "Keep 8 out of 10 shots from finishing long of the back edge.",
        "helps": "Long approach misses, distance discipline, and avoiding over-clubbed shots.",
    },
    "Approach Left": {
        "name": "Approach Start-Line Gate Drill",
        "setup": "Set an alignment stick or visual gate a few yards in front of the ball on your intended start line.",
        "execution": "Hit 10 approach shots focusing only on starting the ball through the intended window.",
        "goal": "Start 7 out of 10 shots on the intended line.",
        "helps": "Left approach misses, poor start line, and face/path control.",
    },
    "Approach Right": {
        "name": "Face-Control Approach Drill",
        "setup": "Pick a target and create a start-line window. Use a mid-iron or scoring club.",
        "execution": "Hit 10 shots with a three-quarter finish. Focus on starting the ball at the target and holding your finish.",
        "goal": "Start 7 out of 10 shots inside the window without a right-side leak.",
        "helps": "Right approach misses, face control, and committed approach swings.",
    },
    "Approach Bad Swing": {
        "name": "Three-Quarter Contact Drill",
        "setup": "Choose a comfortable approach distance and take one more club than usual.",
        "execution": "Hit 10 three-quarter approach shots with a balanced finish. Do not chase full distance.",
        "goal": "Strike 8 out of 10 shots solidly before returning to full swings.",
        "helps": "Poor approach contact, rushed tempo, and swing breakdowns under pressure.",
    },
    "Approach Distance Control": {
        "name": "Distance Ladder Approach Drill",
        "setup": "Choose three yardages that commonly appear in your rounds. Use alignment and a clear landing target for each number.",
        "execution": "Hit 3 balls to the short number, 3 to the middle number, and 3 to the long number. Repeat the ladder twice. Track whether each ball finishes pin-high, short, or long.",
        "goal": "Get at least 6 out of 9 balls finishing within a playable distance window.",
        "helps": "Carry control, club selection, and reducing short/long approach misses.",
    },
    "Approach Accuracy": {
        "name": "Green-Center Discipline Drill",
        "setup": "Pick three approach distances. Instead of aiming at pins, choose the center of the green or the safest section of the target.",
        "execution": "Hit 5 balls from each distance. Score each ball as green hit, safe miss, or short-side/big miss.",
        "goal": "Hit or safely miss 10 out of 15 shots before moving to harder targets.",
        "helps": "Approach discipline, target selection, and avoiding short-sided misses.",
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
    "Death Star Putting": {
        "name": "Death Star Putting Drill",
        "setup": "Place 6 to 8 balls or tees in a circle around the hole. Start at 3 feet. Advanced players can repeat the same circle from 6 feet and 9 feet.",
        "execution": "Move around the circle and make each putt. If you miss, restart the circle from the beginning.",
        "goal": "Complete the full circle without a miss. For advanced work, complete it at 3 feet, then 6 feet, then 9 feet.",
        "helps": "Short-putt conversion, pressure putting, start line, and face control.",
    },
    "Short Game Chipping": {
        "name": "Landing Spot Towel Drill",
        "setup": "Place a small towel on the green where you want the ball to land. Choose 3 common chipping lies.",
        "execution": "Hit 5 chips from each lie trying to land the ball on the towel and let it release toward the hole.",
        "goal": "Land 10 out of 15 chips on or near the towel.",
        "helps": "Chipping contact, landing spot control, and predictable rollout.",
    },
    "Short Game Both": {
        "name": "Up-and-Down Challenge",
        "setup": "Pick 9 short-game spots around a practice green: easy, medium, and difficult lies.",
        "execution": "Play one ball from each spot and finish the hole. Track whether you get up and down. Use your normal pre-shot routine on every attempt.",
        "goal": "Get up and down at least 4 out of 9 times, then work toward 5 or 6.",
        "helps": "Chipping execution, recovery putting, and converting missed greens into pars.",
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
    "Club Selection": {
        "name": "Middle-of-Green Club Selection Drill",
        "setup": "Pick approach targets where being short or long creates a difficult next shot. Use the club that carries to the middle of the green.",
        "execution": "Hit 10 approach shots and track whether your club choice gave you a safe result, even when the strike was not perfect.",
        "goal": "Get 7 out of 10 shots finishing in a safe zone.",
        "helps": "Club selection, distance honesty, and reducing avoidable short/long misses.",
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


def _gap_score(value, reference_key):
    ref = PGA_REFERENCES[reference_key]
    tour_average = ref["tour_average"]

    if ref["higher_is_better"]:
        gap = tour_average - value
    else:
        gap = value - tour_average

    if gap <= 0:
        severity = 0
        label = "Strength"
    elif gap <= 10:
        severity = 1
        label = "Small Gap"
    elif gap <= 25:
        severity = 2
        label = "Moderate Gap"
    else:
        severity = 3
        label = "Major Gap"

    return {
        "gap": round(gap, 1),
        "severity": severity,
        "label": label,
    }


def _format_value(value, reference_key):
    ref = PGA_REFERENCES[reference_key]
    unit = ref["unit"]
    return f"{value}{unit}" if unit else str(value)


def _compare_to_pga(value, reference_key):
    ref = PGA_REFERENCES[reference_key]
    gap_data = _gap_score(value, reference_key)

    if gap_data["severity"] == 0:
        status = "This compares well against the PGA Tour average reference and should be treated as a strength from this round."
    elif gap_data["severity"] == 1:
        status = "This is close to the PGA Tour average reference, but still represents a small scoring opportunity."
    elif gap_data["severity"] == 2:
        status = "This is a meaningful gap relative to PGA Tour benchmarks and should receive practice attention."
    else:
        status = "This is a major gap relative to PGA Tour benchmarks and is likely one of the biggest scoring separators from this round."

    return {
        "label": ref["label"],
        "player_value": _format_value(value, reference_key),
        "top_10": _format_value(ref["top_10"], reference_key),
        "top_50": _format_value(ref["top_50"], reference_key),
        "tour_average": _format_value(ref["tour_average"], reference_key),
        "status": status,
        "gap_label": gap_data["label"],
        "gap": gap_data["gap"],
        "severity": gap_data["severity"],
    }


def _add_unique(items, item):
    if item not in items:
        items.append(item)


def _ranked_weaknesses(
    fairway_pct,
    gir_pct,
    putts,
    penalties,
    up_down_pct,
    up_and_down_chances,
    three_putts,
    tee_box_miss,
    approach_miss,
    round_issue,
):
    weaknesses = []

    fairway_gap = _gap_score(fairway_pct, "fairways")
    gir_gap = _gap_score(gir_pct, "gir")
    putt_gap = _gap_score(putts, "putts")
    penalty_gap = _gap_score(penalties, "penalties")

    weaknesses.append({
        "focus": "Tee Box Accuracy",
        "score": fairway_gap["severity"] * 3 + (2 if tee_box_miss != "No Issues" else 0),
        "text": "Tee box accuracy created pressure. Too many holes likely started from recovery positions.",
    })

    weaknesses.append({
        "focus": "Approach Play",
        "score": gir_gap["severity"] * 3 + (2 if approach_miss != "No Issues" else 0),
        "text": "Approach play was a major scoring leak. Missing greens at this rate forces the short game to carry too much of the round.",
    })

    weaknesses.append({
        "focus": "Putting",
        "score": putt_gap["severity"] * 3 + (2 if three_putts >= 2 else 0),
        "text": "Putting cost strokes. This usually points to poor speed control, missed short putts, or too many long second putts.",
    })

    weaknesses.append({
        "focus": "Course Management",
        "score": penalty_gap["severity"] * 3,
        "text": "Penalty strokes had a major impact. These are high-cost mistakes that should be reduced before chasing aggressive scoring.",
    })

    if up_and_down_chances > 0:
        scramble_gap = _gap_score(up_down_pct, "scrambling")
        weaknesses.append({
            "focus": "Short Game",
            "score": scramble_gap["severity"] * 3,
            "text": "Scrambling was below target. Missed greens were turning into bogeys too often.",
        })

    issue_boosts = {
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

    if round_issue in issue_boosts:
        boosted_focus = issue_boosts[round_issue]

        for item in weaknesses:
            if item["focus"] == boosted_focus:
                item["score"] += 2

        if round_issue == "Poor Short Game - Both":
            for item in weaknesses:
                if item["focus"] == "Putting":
                    item["score"] += 2

    if tee_box_miss != "No Issues":
        weaknesses.append({
            "focus": "Tee Box Accuracy",
            "score": 2,
            "text": f"Your main tee box miss was {tee_box_miss.lower()}. That pattern should guide the tee-shot drill selection.",
        })

    if approach_miss != "No Issues":
        weaknesses.append({
            "focus": "Approach Play",
            "score": 2,
            "text": f"Your main approach miss was {approach_miss.lower()}. That matters because approach play is one of the largest scoring separators.",
        })

    if round_issue != "No Major Issues":
        weaknesses.append({
            "focus": issue_boosts.get(round_issue, "Course Management"),
            "score": 2,
            "text": f"You identified {round_issue.lower()} as a round trend. That self-scouting input should influence the practice plan.",
        })

    filtered = [item for item in weaknesses if item["score"] > 0]
    filtered.sort(key=lambda item: item["score"], reverse=True)

    final_texts = []
    seen_texts = set()

    for item in filtered:
        if item["text"] not in seen_texts:
            final_texts.append(item["text"])
            seen_texts.add(item["text"])

    return filtered, final_texts[:4]


def _build_strengths(fairway_pct, gir_pct, putts, penalties, up_down_pct, up_and_down_chances):
    strengths = []

    if _gap_score(fairway_pct, "fairways")["severity"] == 0:
        _add_unique(strengths, "Tee box accuracy compared well against the PGA Tour average reference. You put yourself in enough playable positions to keep the round organized.")

    if _gap_score(gir_pct, "gir")["severity"] == 0:
        _add_unique(strengths, "Approach play compared well against the PGA Tour average reference. Hitting greens keeps pressure off the short game.")

    if _gap_score(putts, "putts")["severity"] == 0:
        _add_unique(strengths, "Putting volume compared well against the PGA Tour average reference. A putt total in this range usually means you avoided giving away strokes on the greens.")

    if penalties == 0:
        _add_unique(strengths, "You avoided penalty strokes, which protects the scorecard and keeps momentum stable.")

    if up_and_down_chances > 0 and _gap_score(up_down_pct, "scrambling")["severity"] == 0:
        _add_unique(strengths, "Scrambling compared well against the PGA Tour average reference. You turned missed greens into saves at a strong rate.")

    if not strengths:
        strengths.append("No statistical category stood out as a true strength in this round. The focus should be on stabilizing the biggest scoring leaks first.")

    return strengths[:4]


def _focuses_from_ranked_weaknesses(ranked_weaknesses):
    if not ranked_weaknesses:
        return ["Consistency"]

    focus_scores = {}

    for item in ranked_weaknesses:
        focus = item["focus"]
        focus_scores[focus] = focus_scores.get(focus, 0) + item["score"]

    if not focus_scores:
        return ["Consistency"]

    sorted_focuses = sorted(focus_scores.items(), key=lambda item: item[1], reverse=True)
    top_focus, top_score = sorted_focuses[0]

    if len(sorted_focuses) == 1:
        return [top_focus]

    second_focus, second_score = sorted_focuses[1]

    if top_score <= 0:
        return ["Consistency"]

    if top_focus == "Short Game" and second_focus == "Putting":
        return ["Short Game"]

    if top_focus == "Putting" and second_focus == "Short Game":
        return ["Short Game"]

    if second_score >= top_score - 2 and second_score >= 4:
        return [top_focus, second_focus]

    return [top_focus]


def _select_drill_for_focus(focus, tee_box_miss, approach_miss, round_issue):
    if focus == "Tee Box Accuracy":
        if tee_box_miss == "Right":
            return DRILLS["Tee Box Right Miss"]
        if tee_box_miss == "Left":
            return DRILLS["Tee Box Left Miss"]
        if tee_box_miss == "Short":
            return DRILLS["Tee Box Short"]
        if tee_box_miss == "Long":
            return DRILLS["Tee Box Long"]
        if tee_box_miss == "Penalty Trouble":
            return DRILLS["Tee Box Penalty Trouble"]
        if tee_box_miss == "Inconsistent":
            return DRILLS["Tee Box Inconsistent"]
        if tee_box_miss == "Bad Swing":
            return DRILLS["Tee Box Bad Swing"]
        return DRILLS["Tee Box Inconsistent"]

    if focus == "Approach Play":
        if round_issue == "Poor Approach Distance Control":
            return DRILLS["Approach Distance Control"]
        if round_issue == "Poor Approach Accuracy":
            return DRILLS["Approach Accuracy"]
        if approach_miss == "Short":
            return DRILLS["Approach Short"]
        if approach_miss == "Long":
            return DRILLS["Approach Long"]
        if approach_miss == "Left":
            return DRILLS["Approach Left"]
        if approach_miss == "Right":
            return DRILLS["Approach Right"]
        if approach_miss == "Bad Swing":
            return DRILLS["Approach Bad Swing"]
        return DRILLS["Approach Accuracy"]

    if focus == "Putting":
        if round_issue == "Poor Putting Speed":
            return DRILLS["Putting Speed"]
        if round_issue == "Poor Putting Start Line":
            return DRILLS["Putting Start Line"]
        if round_issue == "Poor Putting Green Reading":
            return DRILLS["Putting Green Reading"]
        if round_issue == "Poor Short Game - Putting":
            return DRILLS["Death Star Putting"]
        return DRILLS["Putting Speed"]

    if focus == "Short Game":
        if round_issue == "Poor Short Game - Chipping":
            return DRILLS["Short Game Chipping"]
        if round_issue == "Poor Short Game - Both":
            return DRILLS["Short Game Both"]
        return DRILLS["Short Game Both"]

    if focus == "Course Management":
        if round_issue == "Too Many Penalties":
            return DRILLS["Penalties"]
        if round_issue == "Bad Club Selection":
            return DRILLS["Club Selection"]
        if round_issue == "Poor Course Management":
            return DRILLS["Course Management"]
        if round_issue == "Struggled Under Pressure":
            return DRILLS["Pressure"]
        if round_issue == "Slow Start":
            return DRILLS["Slow Start"]
        if round_issue == "Poor Finish":
            return DRILLS["Poor Finish"]
        return DRILLS["Course Management"]

    return DRILLS["Approach Accuracy"]


def _build_practice_plan(primary_focuses, tee_box_miss, approach_miss, round_issue):
    drills = []

    for focus in primary_focuses:
        drill = _select_drill_for_focus(focus, tee_box_miss, approach_miss, round_issue)

        if drill not in drills:
            drills.append(drill)

    if len(drills) == 0:
        drills.append(DRILLS["Approach Accuracy"])

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

    strengths = _build_strengths(
        fairway_pct,
        gir_pct,
        putts,
        penalties,
        up_down_pct,
        up_and_down_chances,
    )

    ranked_weaknesses, weaknesses = _ranked_weaknesses(
        fairway_pct,
        gir_pct,
        putts,
        penalties,
        up_down_pct,
        up_and_down_chances,
        three_putts,
        tee_box_miss,
        approach_miss,
        round_issue,
    )

    primary_focuses = _focuses_from_ranked_weaknesses(ranked_weaknesses)
    practice_plan = _build_practice_plan(primary_focuses, tee_box_miss, approach_miss, round_issue)

    if len(primary_focuses) == 1:
        focus_text = primary_focuses[0]
    else:
        focus_text = " + ".join(primary_focuses)

    pattern_sentences = []

    if tee_box_miss != "No Issues":
        pattern_sentences.append(f"Your tee box miss pattern was {tee_box_miss.lower()}.")

    if approach_miss != "No Issues":
        pattern_sentences.append(f"Your approach miss pattern was {approach_miss.lower()}.")

    if round_issue != "No Major Issues":
        pattern_sentences.append(f"The round trend you identified was {round_issue.lower()}.")

    if pattern_sentences:
        pattern_text = " ".join(pattern_sentences)
    else:
        pattern_text = "There was no major miss pattern selected, so the report is driven primarily by your scoring statistics."

    if len(primary_focuses) == 1:
        focus_sentence = f"Your primary focus is {focus_text.lower()}."
    else:
        focus_sentence = f"Your primary focuses are {focus_text.lower()}."

    coach_insight = (
        f"{round_tier['description']} {focus_sentence} "
        f"{pattern_text} The practice plan below is built around the most direct fixes for the scoring leaks shown in this round."
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
        "strengths": strengths,
        "weaknesses": weaknesses,
        "practice_plan": practice_plan,
        "tee_box_miss": tee_box_miss,
        "approach_miss": approach_miss,
        "round_issue": round_issue,
        "pga_comparisons": pga_comparisons,
    }
