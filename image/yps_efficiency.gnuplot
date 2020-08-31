reset
dx=1.0
n=2
total_box_width_relative=0.75
gap_width_relative=0.1
d_width=(gap_width_relative+total_box_width_relative)*dx/2.
reset
set term png truecolor size 1280, 640
set size 1.0, 1.0
set title "Single and Accumulative Efficiency: YespowerSugar Performance\n CPU: Ryzen 1700 (Stock), RAM: DDR4 2400 MT/s\n Version=1.0.1 N=2048 r=32, Using 8192.00 KiB RAM"

set key box left top
set key width 1 height 1
#set key font ",9"

set xlabel "Threads Amount (t)"
set ylabel "Hashrate (h/s)"
set xrange [0:17]
set yrange [0:1100]
set xtics 1,1,16
set ytics 0,100,1000
set grid
set boxwidth total_box_width_relative/n relative
set style fill transparent solid 0.5 noborder
set output "yps_efficiency.png"
plot "yps_efficiency.csv" u ($1-0.25):2 w boxes lc rgb"green" title "Single Thread",\
     "yps_efficiency.csv" u ($1+d_width-0.25):3 w boxes lc rgb"red" title "Accumulative"
