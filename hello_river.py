from river import anomaly

detector = anomaly.HalfSpaceTrees(seed=42)

score = detector.score_one({'value': 10})
print(f"Puntuación de anomalía: {score}")
