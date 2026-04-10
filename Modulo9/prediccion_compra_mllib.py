# ============================================
# PROYECTO: Predicción de compra con MLlib
# ============================================

from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.evaluation import BinaryClassificationEvaluator
from pyspark.ml.tuning import CrossValidator, ParamGridBuilder

# =============================
# 1. CREAR SESIÓN
# =============================
spark = SparkSession.builder.appName("MLlib_Ecommerce").getOrCreate()

# =============================
# 2. DATASET SIMULADO
# =============================
data = spark.createDataFrame([
    (25, 5, 100, 1),
    (40, 2, 200, 0),
    (30, 10, 300, 1),
    (22, 1, 50, 0),
    (35, 7, 250, 1)
], ["edad", "visitas", "gasto", "compra"])

# =============================
# 3. VECTOR DE FEATURES
# =============================
assembler = VectorAssembler(
    inputCols=["edad", "visitas", "gasto"],
    outputCol="features"
)

data = assembler.transform(data)

# =============================
# 4. TRAIN / TEST
# =============================
train, test = data.randomSplit([0.8, 0.2], seed=42)

# =============================
# 5. MODELO (Regresión Logística)
# =============================
lr = LogisticRegression(labelCol="compra")

# =============================
# 6. GRID SEARCH
# =============================
paramGrid = ParamGridBuilder() \
    .addGrid(lr.regParam, [0.01, 0.1]) \
    .addGrid(lr.maxIter, [10, 20]) \
    .build()

evaluator = BinaryClassificationEvaluator(
    labelCol="compra",
    metricName="areaUnderROC"
)

crossval = CrossValidator(
    estimator=lr,
    estimatorParamMaps=paramGrid,
    evaluator=evaluator,
    numFolds=3
)

# =============================
# 7. ENTRENAMIENTO
# =============================
model = crossval.fit(train)

# =============================
# 8. PREDICCIÓN
# =============================
predictions = model.transform(test)
predictions.select("features", "compra", "prediction").show()

# =============================
# 9. EVALUACIÓN
# =============================
auc = evaluator.evaluate(predictions)
print("AUC ROC:", auc)