from src.load_data import load_osm_data
from src.visualize_map import plot_map

# โหลดถนนโซนสยาม
G = load_osm_data("Siam Square, Bangkok, Thailand")

# วาดแผนที่
plot_map(G)