
# Month 1 summary

## Question
Which areas of AMAC lie within 200m of a watercourse?

## Operation
Buffered WATERWAY features by 200m, dissolved the overlapping buffer polygons, then took the spatial intersection/difference against ward boundaries and calculated the percentage of each ward falling within the buffer zone.

## Expected
Expected only two or three peripheral wards to have significant overlap with the 200m waterway buffer, with most urbanized central areas falling outside the zone.

## Got
Out of 23,086 total buffered settlement points in AMAC, 4,654 fall within 200m of a waterway (approximately 20.16% of settlements). 

## What surprised me
A higher proportion of  flooded settlements than I expected sit directly in high traffic urban areas .

## Limitations, stated plainly
- settlement data Was incomplete or inconsistent in spatial coverage across  wards.

## What I still need
- Population per ward, to convert the area or settlement counts into total population affected, which is the metric that truly matters for planning.


![200M BUFFER](<200M WATER WAY BUFFER-1.png>)

