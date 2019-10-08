def fun():
    import math
    print("Angulo de 45°\t90°\t180°")
    print("=====================")
    print("sin(x)  %.2f \t" % (math.sin(math.radians(45))))
    print("%.2f \t" % (math.sin(math.radians(90))))
    print("%.2f " % (math.sin(math.radians(180))))
    print("cos(x)  %.2f \t" % (math.cos(math.radians(45))))
    print("%.2f \t" % (math.cos(math.radians(90))))
    print("%.2f " % (math.cos(math.radians(180))))

fun()

