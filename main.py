import netCDF4

# 1. calculate speeds for every xy
# 2. do color scales and make that a ppm file
# 3. use geotiff instead
# 4. use angles to do gradients

def main(f):
    velX = f.variables['VX']
    velY = f.variables['VY']
    velXArray = velX[:]
    velYArray = velY[:]
    speed = (velX * velX + velY * velY) ** 0.5

with netCDF4.Dataset('data/antarctica_ice_velocity_450m_v2.nc') as f:
    main(f)
