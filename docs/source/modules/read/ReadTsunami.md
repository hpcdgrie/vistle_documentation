
# ReadTsunami
read ChEESE Tsunami files

<svg width="80.0em" height="10.6em" >
<style>.text { font: normal 1.0em sans-serif;}tspan{ font: italic 1.0em sans-serif;}.moduleName{ font: bold 1.0em sans-serif;}</style>
<rect x="0em" y="0.8em" width="8.0em" height="3.0em" rx="0.1em" ry="0.1em" style="fill:#64c8c8ff;" />
<text x="0.2em" y="2.6500000000000004em" class="moduleName" >ReadTsunami</text><rect x="0.2em" y="2.8em" width="1.0em" height="1.0em" rx="0.0em" ry="0.0em" style="fill:#c8c81eff;" >
<title>Sea surface</title></rect>
<rect x="0.7em" y="3.8em" width="0.03333333333333333em" height="6.0em" rx="0.0em" ry="0.0em" style="fill:#000000;" />
<rect x="0.7em" y="9.8em" width="1.0em" height="0.03333333333333333em" rx="0.0em" ry="0.0em" style="fill:#000000;" />
<text x="1.9em" y="9.9em" class="text" >Grid Sea (Heightmap/LayerGrid)<tspan> (Sea surface)</tspan></text>
<rect x="1.4em" y="2.8em" width="1.0em" height="1.0em" rx="0.0em" ry="0.0em" style="fill:#c8c81eff;" >
<title>Ground surface</title></rect>
<rect x="1.9em" y="3.8em" width="0.03333333333333333em" height="5.0em" rx="0.0em" ry="0.0em" style="fill:#000000;" />
<rect x="1.9em" y="8.8em" width="1.0em" height="0.03333333333333333em" rx="0.0em" ry="0.0em" style="fill:#000000;" />
<text x="3.0999999999999996em" y="8.9em" class="text" >Sea floor (Heightmap/LayerGrid)<tspan> (Ground surface)</tspan></text>
<rect x="2.5999999999999996em" y="2.8em" width="1.0em" height="1.0em" rx="0.0em" ry="0.0em" style="fill:#c8c81eff;" >
<title>scalar_port_0</title></rect>
<rect x="3.0999999999999996em" y="3.8em" width="0.03333333333333333em" height="4.0em" rx="0.0em" ry="0.0em" style="fill:#000000;" />
<rect x="3.0999999999999996em" y="7.8em" width="1.0em" height="0.03333333333333333em" rx="0.0em" ry="0.0em" style="fill:#000000;" />
<text x="4.3em" y="7.8999999999999995em" class="text" >Port for scalar number 0<tspan> (scalar_port_0)</tspan></text>
<rect x="3.8em" y="2.8em" width="1.0em" height="1.0em" rx="0.0em" ry="0.0em" style="fill:#c8c81eff;" >
<title>scalar_port_1</title></rect>
<rect x="4.3em" y="3.8em" width="0.03333333333333333em" height="3.0em" rx="0.0em" ry="0.0em" style="fill:#000000;" />
<rect x="4.3em" y="6.8em" width="1.0em" height="0.03333333333333333em" rx="0.0em" ry="0.0em" style="fill:#000000;" />
<text x="5.5em" y="6.8999999999999995em" class="text" >Port for scalar number 1<tspan> (scalar_port_1)</tspan></text>
<rect x="5.0em" y="2.8em" width="1.0em" height="1.0em" rx="0.0em" ry="0.0em" style="fill:#c8c81eff;" >
<title>scalar_port_2</title></rect>
<rect x="5.5em" y="3.8em" width="0.03333333333333333em" height="2.0em" rx="0.0em" ry="0.0em" style="fill:#000000;" />
<rect x="5.5em" y="5.8em" width="1.0em" height="0.03333333333333333em" rx="0.0em" ry="0.0em" style="fill:#000000;" />
<text x="6.7em" y="5.8999999999999995em" class="text" >Port for scalar number 2<tspan> (scalar_port_2)</tspan></text>
<rect x="6.2em" y="2.8em" width="1.0em" height="1.0em" rx="0.0em" ry="0.0em" style="fill:#c8c81eff;" >
<title>scalar_port_3</title></rect>
<rect x="6.7em" y="3.8em" width="0.03333333333333333em" height="1.0em" rx="0.0em" ry="0.0em" style="fill:#000000;" />
<rect x="6.7em" y="4.8em" width="1.0em" height="0.03333333333333333em" rx="0.0em" ry="0.0em" style="fill:#000000;" />
<text x="7.9em" y="4.8999999999999995em" class="text" >Port for scalar number 3<tspan> (scalar_port_3)</tspan></text>
</svg>

## Parameters
|name|description|type|
|-|-|-|
|first_step|first timestep to read|Int|
|last_step|last timestep to read (-1: last)|Int|
|step_increment|number of steps to increment|Int|
|first_rank|rank for first partition of first timestep|Int|
|file_dir|NC File directory|String|
|ghost|Show ghostcells.|Int|
|fill|Replace filterValue.|Int|
|VerticalScale|Vertical Scale parameter sea|Float|
|blocks_latitude|number of blocks in lat-direction|Int|
|blocks_longitude|number of blocks in lon-direction|Int|
|fillValue|ncFile fillValue offset for eta|Float|
|fillValueNew|set new fillValue offset for eta|Float|
|bathymetry|Select bathymetry stored in netCDF)|String|
|scalar_0|Select scalar.)|String|
|scalar_1|Select scalar.)|String|
|scalar_2|Select scalar.)|String|
|scalar_3|Select scalar.)|String|
