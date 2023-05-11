import cv2
import fingerprint_feature_extractor


if __name__ == '__main__':
    img = cv2.imread('3.jpg', 0)
    FeaturesTerminations, FeaturesBifurcations = fingerprint_feature_extractor.extract_minutiae_features(img, spuriousMinutiaeThresh=10, invertImage = False, showResult=True, saveResult = True)