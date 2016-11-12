package io.muic.dcom.p2;
import java.util.*;

/**
 * Created by Don on 11/11/2016 AD.
 */
public class id implements Runnable{
    @Override
    public void run() {

    }

    public static class ParcelObserved {
        private String parcelId;
        private String stationId;
        private long timeStamp;

        ParcelObserved(String parcelId_, String stationId_, long ts_) {
            this.parcelId = parcelId_;
            this.stationId = stationId_;
            this.timeStamp = ts_;
        }

        public String getParcelId() { return parcelId; }
        public String getStationId() { return stationId; }
        public long getTimeStamp() { return timeStamp; }
    }

    private Map<String,Map<String,Long>> transactions;

    id(){
        transactions = new HashMap<>();
    }
    public void postObserve(String parcelId, String stationId, long timestamp) {
        Map<String,Long> temporary = new HashMap<>();
        temporary.put(stationId,timestamp);
        transactions.put(parcelId, temporary);
    }

    public List<String> getParcelTrail(String parcelId) {
        List<String> ans = new ArrayList<>();
        if (transactions.containsKey(parcelId)) {
            ans.add(transactions.values().iterator().next().keySet().iterator().next());
        }
        return ans;
    }

    public long getStopCount(String stationId) {
        long count=0;
        if (transactions.values().iterator().next().containsKey(stationId)){
            count++;
        }
        return count;
    }
}
