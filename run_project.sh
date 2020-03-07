OUTPUT1=$(python execute.py --image concert.jpg && python calculate_optical_flow.py --image concert.jpg)
OUTPUT2=$(python execute.py --image group.jpg && python calculate_optical_flow.py --image group.jpg)
OUTPUT3=$(python execute.py --image trooper.jpg && python calculate_optical_flow.py --image trooper.jpg)

python deterministic_stochastic.py --det_coeff 0.6 --stoc_coeff 0.4 --input1 "$OUTPUT1" --input2 "$OUTPUT2" --input3 "$OUTPUT3"

echo "$OUTPUT1\n$OUTPUT2\n$OUTPUT3" > output.log
