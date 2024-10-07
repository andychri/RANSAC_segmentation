import numpy as np
import open3d as o3d
import matplotlib.pyplot as plt

DATANAME = "box_filter2.pcd"
#DATANAME = "appartment_cloud.ply"
pcd = o3d.io.read_point_cloud("/home/andreas/Desktop/" + DATANAME)

pcd_center = pcd.get_center()
pcd.translate(-pcd_center)

nn = 16
std_multiplier =10

filtered_pcd = pcd.remove_statistical_outlier(nn, std_multiplier)

outliers = pcd.select_by_index(filtered_pcd[1], invert=True)
outliers.paint_uniform_color([1, 0, 0])
filtered_pcd = filtered_pcd[0]

#o3d.visualization.draw_geometries([filtered_pcd, outliers])

voxel_size = 0.01
pcd_downsampled = filtered_pcd.voxel_down_sample(voxel_size = voxel_size)
#o3d.visualization.draw_geometries([pcd_downsampled])

nn_distance = np.mean(pcd.compute_nearest_neighbor_distance())

radius_normals = nn_distance*4

pcd_downsampled.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=radius_normals, max_nn = 16), fast_normal_computation = True)

pcd_downsampled.paint_uniform_color([0.6, 0.6, 0.6])
o3d.visualization.draw_geometries([pcd_downsampled, outliers])

#front =
#ookat = 
#up =
#zoom =

#o3d.visualization.draw_geometries([pcd_downsampled])

max_plane_idx = 6
pt_to_plane_dist = 0.02

segment_models = {}
segments = ()
rest = pcd

#for i in range(max_plane_idx):
#    colors.plt.get_cmap("tab20")(i)
#    segment_models[i], inliers = rest.segment_plane(distance_threshold)
