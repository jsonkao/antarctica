## Data Diary

### Antarctica Ice Velocity

* Source: [MEaSUREs InSAR-Based Antarctica Ice Velocity Map](https://nsidc.org/data/nsidc-0484) from the [NSIDC](https://nsidc.org).

Data is the NetCDF file `antarctica_ice_velocity_450m_v2.nc`. The original is kept in the `antarctica_ice_velocity_450m_v2` directory. The duplicate for reading into Python is in the `data` directory.

- speed = √(vx^2 + vy^2)
- angle = arctan (vy / vx)
