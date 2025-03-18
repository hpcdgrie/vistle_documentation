
# MiniSim
small simulation to compare performance with other in situ interfaces

<svg width="50.599999999999994em" height="4.6em" >
<style>.text { font: normal 1.0em sans-serif;}tspan{ font: italic 1.0em sans-serif;}.moduleName{ font: bold 1.0em sans-serif;}</style>
<rect x="0em" y="0.8em" width="5.06em" height="3.0em" rx="0.1em" ry="0.1em" style="fill:#64c8c8ff;" />
<text x="0.2em" y="2.6500000000000004em" class="moduleName" >MiniSim</text></svg>

## Parameters
|name|description|type|
|-|-|-|
|input_params|path to file with input parameters|String|
|num_timesteps|maximum number of timesteps to execute|Int|
|numThreads|number of threads used by the sim|Int|
|numGhost|number of ghost cells in each direction|Int|
|numParticles|number of particles|Int|
|numBlocks|number of overall blocks, if zero mpi size is used|Int|
|verbose|print debug messages|Int|
|sync|synchronize after each timestep|Int|
|velocityScale|scale factor to convert function gradient to velocity|Float|
|tEnd|end time|Float|
|dt|time step length|Float|
|frequency|the pipeline is processed for every nth simulation cycle|Int|
|keep_timesteps|if true timesteps are cached and processed as time series|Int|
|path|path to the connection file written by the simulation|String|
