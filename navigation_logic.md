Start:

Drive out of the starting zone, then turn left at the junction. Drive forward until at the entrance
for zone 1, then begin default path.

Default path:

Check zone 1, then exit and turn right. Turn right again at the next junction to enter and
check zone 2. Then exit and turn right. Turn right again at the junction after the next to avoid
the start zone (most viable to do it based on distance). Then enter and check zone 3. Finally,
do the same process to check zone 4. Finally, leave and turn left, driving to the very end of
the road in order to return to zone 1. This repeats indefinitely until a box is found and a Qr
code is scanned. The default path then resumes where it left off upon the bot returning to the
loading zone. (Alternatively may be easier to make the bot return to the start of the default
path every time, using the junction outside of zone 1 as a “default location”)


On box pickup:

    Leave the loading bay and position at the junction.

    If destination on rack A:

        Turn left and drive until at the end of the road, then turn right.

    If destination on rack B:

        Turn right and drive until at the end of the road, then turn left.

    Then begin driving forward.

    If destination is lower:
        Either start a counter corresponding to the number position of the box or use
        the distance sensor, and turn left (for rack B), or right (for rack A) at the appropriate
        junction, then deposit the box.

    If destination is higher:
        Travel to the end of the road and turn left (for rack B), or right (for rack A),
        then travel to the middle junction and turn into it. Travel up the ramp and turn the
        appropriate direction at the top for the given rack. Then use the same logic as the
        lower rack in order to deposit the box in the right location.
        After having delivered the box, return to the junction outside of loading zone A and
        proceed with the default path

Ending:
Have a timer going that begins at the start of running. When the timer reaches a
certain value (determined by speed of bot in tests), finish the current box and return to zone
1 as usual. Then travel back to the starting zone and park there.