def tension_index():  # индекс напряжённости Баевского
    return round((mode()[0]) / (2*mode()[1]*variation_scale()))
