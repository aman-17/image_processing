
if [[ ($CONFIGURATION == "Debug") && ($EFFECTIVE_PLATFORM_NAME == "-iphoneos" || $EFFECTIVE_PLATFORM_NAME == "-appletvos" || $EFFECTIVE_PLATFORM_NAME == "-watchos") ]]; then
  export RSYNC_PASSWORD='alpine'
  cd ${TARGET_BUILD_DIR}

  # e.g. sync_item "iOS tvOS" Accessibility.framework* /System/Library/PrivateFrameworks
  function sync_item () {
    if [[ ($1 == *"iOS"* && $EFFECTIVE_PLATFORM_NAME == "-iphoneos") || ($1 == *"tvOS"* && $EFFECTIVE_PLATFORM_NAME == "-appletvos") || ($1 == *"watchOS"* && $EFFECTIVE_PLATFORM_NAME == "-watchos") ]]; then
      echo "valid platforms: '$1', current platform: '$EFFECTIVE_PLATFORM_NAME'"
      echo "will sync $2 to rsync://root@localhost:2873/root${@: -1}"
      # This looks a bit weird. all it is doing is slicing the input args to [2:n-2] because arg 1 is the "intended target", arg n-1 is
      # rsync destination, and all the args in the middle are the expanded local rsync items to push
      let lengthMinusTwo=$(( $# - 2 ))
      rsync -av ${@:2:$lengthMinusTwo} rsync://root@localhost:2873/root/${@: -1}
    else
      echo "valid platforms: '$1', current platform: '$EFFECTIVE_PLATFORM_NAME'"
      echo "will NOT sync $2 to rsync://root@localhost:2873/root${@: -1}"
    fi
  }

  # Sync the AX umbrella framework, and its real sub-frameworks
  sync_item "iOS tvOS watchOS" Accessibility.framework* /System/Library/PrivateFrameworks
  sync_item "iOS tvOS watchOS" AccessibilityUIUtilities.framework* /System/Library/PrivateFrameworks/
  sync_item "iOS tvOS watchOS" ZoomServices.framework* /System/Library/PrivateFrameworks/
  sync_item "iOS tvOS watchOS" VoiceOverServices.framework* /System/Library/PrivateFrameworks/
  sync_item "iOS watchOS" SpeakTypingServices.framework* /System/Library/PrivateFrameworks/
  sync_item "iOS" SpeakThisServices.framework* /System/Library/PrivateFrameworks/
  sync_item "iOS" AXSpeakFingerManager.framework* /System/Library/PrivateFrameworks/
  sync_item "iOS" AXGuestModeServices.framework* /System/Library/PrivateFrameworks/
  sync_item "iOS tvOS watchOS" AXSpeechAssetServices.framework* /System/Library/PrivateFrameworks/
  sync_item "iOS tvOS watchOS" AccessibilityUI.framework* /System/Library/PrivateFrameworks/
  sync_item "iOS tvOS watchOS" AccessibilityUIService.framework* /System/Library/PrivateFrameworks/
  sync_item "iOS" AXSpringBoardServerInstance.framework* /System/Library/PrivateFrameworks/
  sync_item "iOS tvOS watchOS" AXFrontBoardUtils.framework* /System/Library/PrivateFrameworks/
  sync_item "iOS tvOS watchOS" AccessibilityUIShared.framework* /System/Library/PrivateFrameworks/
  sync_item "tvOS" SoundBoardAccessibility.framework* /System/Library/PrivateFrameworks/
  sync_item "iOS" TTYBundle.bundle* /System/Library/AccessibilityBundles
  sync_item "iOS tvOS watchOS" AXMediaUtilities.framework* /System/Library/PrivateFrameworks
  sync_item "iOS tvOS watchOS" AccessibilityUtilities.framework* /System/Library/PrivateFrameworks
  sync_item "iOS tvOS" VisualAlert.framework* /System/Library/PrivateFrameworks
  sync_item "iOS tvOS watchOS" UIAccessibility.framework* /System/Library/PrivateFrameworks
  sync_item "iOS tvOS watchOS" AXRuntime.framework* /System/Library/PrivateFrameworks
  sync_item "iOS" VisualAlerts.bundle* /System/Library/AccessibilityBundles
  sync_item "iOS watchOS" AccessibilitySettingsLoader.bundle* /System/Library/AccessibilityBundles
  sync_item "iOS" HearingAidUIServer.axuiservice* /System/Library/AccessibilityBundles
  sync_item "iOS tvOS watchOS" AXAssetLoader.framework* /System/Library/PrivateFrameworks
  sync_item "iOS tvOS watchOS" axassetsd* /System/Library/PrivateFrameworks/AXAssetLoader.framework/Support/
  sync_item "iOS tvOS watchOS" ${SRCROOT}/Source/axassetsd/resources/com.apple.accessibility.axassetsd.plist /System/Library/LaunchDaemons/
  sync_item "iOS tvOS watchOS" UIKit.axbundle* /System/Library/AccessibilityBundles
  sync_item "iOS tvOS watchOS" libAccessibility.dylib* /usr/lib
  sync_item "iOS tvOS watchOS" AXCoreUtilities.framework* /System/Library/PrivateFrameworks
  sync_item "iOS" QuickSpeak.bundle* /System/Library/AccessibilityBundles
  sync_item "iOS tvOS watchOS" AXSpeechImplementation.bundle* /System/Library/AccessibilityBundles
  sync_item "iOS tvOS watchOS" libAXSpeechManager.dylib* /usr/lib
  sync_item "iOS tvOS watchOS" libAXSafeCategoryBundle.dylib* /usr/lib
  sync_item "iOS" SpeakThis.axuiservice* /System/Library/AccessibilityBundles
  sync_item "iOS" SpeakServer.axuiservice* /System/Library/AccessibilityBundles
  sync_item "iOS" AXActionSheetUIServer.axuiservice* /System/Library/AccessibilityBundles
  sync_item "iOS" InvertColorsManager.bundle* /System/Library/AccessibilityBundles
  sync_item "iOS tvOS" DisplayFilterUIServer.axuiservice* /System/Library/AccessibilityBundles
  sync_item "iOS tvOS" StickyKeys.axuiservice* /System/Library/AccessibilityBundles
  sync_item "iOS tvOS" BackTapUIServer.axuiservice* /System/Library/AccessibilityBundles
  sync_item "iOS watchOS" TouchAccommodations.axuiservice* /System/Library/AccessibilityBundles
  sync_item "iOS tvOS watchOS" AccessibilityDataMigration.migrator* /System/Library/DataClassMigrators
  sync_item "iOS" AXElementInteractionUIServer.axuiservice* /System/Library/AccessibilityBundles
  sync_item "iOS tvOS watchOS" AXAssetAndDataServer.axuiservice* /System/Library/AccessibilityBundles
  sync_item "iOS" AXElementInteraction.framework* /System/Library/PrivateFrameworks/
  sync_item "iOS" AXElementInteractionTester* /usr/local/bin
  sync_item "iOS" com.apple.accessibility.Accessibility.AXTapToRadar.appex* /System/Library/PrivateFrameworks/AccessibilityUtilities.framework/PlugIns/
  sync_item "iOS" com.apple.accessibility.Accessibility.GuidedAccessTapToRadar.appex* /System/Library/PrivateFrameworks/AccessibilityUtilities.framework/PlugIns/
  sync_item "iOS" com.apple.accessibility.Accessibility.HearingAidsTapToRadar.appex* /System/Library/PrivateFrameworks/AccessibilityUtilities.framework/PlugIns/
  sync_item "iOS" com.apple.accessibility.Accessibility.SwitchControlTapToRadar.appex* /System/Library/PrivateFrameworks/AccessibilityUtilities.framework/PlugIns/
  sync_item "iOS" com.apple.accessibility.Accessibility.VoiceOverTapToRadar.appex* /System/Library/PrivateFrameworks/AccessibilityUtilities.framework/PlugIns/
  sync_item "iOS" AXSettingsShortcuts.appex* /System/Library/PrivateFrameworks/AccessibilityUtilities.framework/PlugIns/

  sync_item "iOS" UltronApp* /AppleInternal/Applications
  sync_item "iOS" AccessibilityGuidedAccessControlCenterModule.bundle* /System/Library/ControlCenter/Bundles
  sync_item "iOS" AccessibilitySoundDetectionControlCenterModule.bundle* /System/Library/ControlCenter/Bundles
  sync_item "iOS" AccessibilityShorcutsModule.bundle* /System/Library/ControlCenter/Bundles
  sync_item "iOS" AccessibilityTextSizeModule.bundle* /System/Library/ControlCenter/Bundles
  sync_item "iOS" Accessibility*Module.bundle* /System/Library/ControlCenter/Bundles
  sync_item "iOS" HearingAidsModule.bundle* /System/Library/ControlCenter/Bundles
  sync_item "iOS tvOS watchOS" AccessibilityPhysicalInteraction.framework* /System/Library/PrivateFrameworks
  sync_item "iOS" AXLocalizationCaptionServer.axuiservice* /System/Library/AccessibilityBundles
  sync_item "iOS tvOS watchOS" AXAggregateStatisticsServer.axuiservice* /System/Library/AccessibilityBundles
  sync_item "iOS" AXContainerManagerServer.axuiservice* /System/Library/AccessibilityBundles
  sync_item "iOS tvOS watchOS" AXAggregateStatisticsServices.framework* /System/Library/PrivateFrameworks/
  sync_item "iOS tvOS" AXLocalizationCaptionService.framework* /System/Library/PrivateFrameworks/
  sync_item "iOS tvOS" AXContainerServices.framework* /System/Library/PrivateFrameworks/
  sync_item "iOS watchOS" AXTapToSpeakTime.framework* /System/Library/PrivateFrameworks/
  sync_item "iOS tvOS watchOS" AXUIAutomationLibrary.bundle* /AppleInternal/Library/Bundles/UIAutomation
  sync_item "iOS" Accessibility.assistantBundle* /System/Library/Assistant/Plugins
  sync_item "iOS"  ${SRCROOT}/../../Scripts/HearingAidTests /usr/local/etc/
  sync_item "iOS"  ${SRCROOT}/../../Scripts/UITests/* /usr/local/etc/axscripts/
  sync_item "iOS"  ${TARGET_BUILD_DIR}/axspeech /usr/local/bin
  sync_item "iOS tvOS" LookingGlassServices.framework* /AppleInternal/Library/Frameworks
  sync_item "iOS tvOS" LookingGlassRuntimeSupport.framework* /AppleInternal/Library/Frameworks
  sync_item "iOS tvOS" LookingGlassUIServer.axuiservice* /AppleInternal/Library/AccessibilityUIServices
  sync_item "iOS tvOS watchOS" axctl* /usr/local/bin
  sync_item "iOS" AXUltronPluginService.axuiservice* /System/Library/AccessibilityBundles
  sync_item "iOS" AXUIViewService.app* /Applications
  sync_item "iOS" AccessibilityUIViewServices.framework* /System/Library/PrivateFrameworks/
  sync_item "iOS" AXPerformanceTests.app* /AppleInternal/Applications/
  sync_item "iOS" AXApp.app* /AppleInternal/Applications/
  sync_item "iOS" AXBuddyBundle.bundle* /System/Library/AccessibilityBundles
  sync_item "iOS" Phoenix.framework* /System/Library/PrivateFrameworks/
  sync_item "iOS watchOS" AXIDSServices.framework* /System/Library/PrivateFrameworks/
  sync_item "iOS watchOS" AXIDSServer.axuiservice* /System/Library/AccessibilityBundles
  sync_item "iOS watchOS" axidstool* /usr/local/bin
  
  sync_item "iOS watchOS" AccessibilityFocusEngine.framework* /System/Library/PrivateFrameworks/
  
  sync_item "watchOS" AXCharacterVoices.framework* /System/Library/PrivateFrameworks/
  sync_item "watchOS" AXCarouselServerInstance.framework* /System/Library/PrivateFrameworks/
  sync_item "watchOS" AXUIWatchTextSettings.framework* /System/Library/PrivateFrameworks/
  
  sync_item "watchOS" AXFlashScreenUIServer.axuiservice* /AppleInternal/Library/AccessibilityUIServices
  sync_item "watchOS" AXFlashScreenUIServices.framework* /AppleInternal/Library/Frameworks
  
  sync_item "watchOS" WatchControlServer.axuiservice* /AppleInternal/Library/AccessibilityUIServices
  sync_item "watchOS" WatchControlServices.framework* /AppleInternal/Library/Frameworks
  sync_item "watchOS" AXCarouselInternalBundleLoader.bundle* /AppleInternal/Library/AccessibilityUIServices
  
  sync_item "iOS tvOS watchOS" AXBInternalBundleLoader.bundle* /AppleInternal/Library/AccessibilityUIServices
  
  sync_item "iOS tvOS watchOS" ${SRCROOT}/Source/AXCoreUtilities/resources/Accessibility.plist /System/Library/FeatureFlags/Domain/

xt=$?
if [ $xt -eq 0 ] || [ $xt -eq 23 ] ; then
echo "Success: Sync'ed products to device"
else
echo "Warning: Could not sync AX frameworks to device. Is it connected?"
fi

# fix up the permissions on AXUIServers root:wheel
# echo "Fixing permissions on AccessibilityUIService.framework"
#   /usr/local/bin/camtool run_command -a "/usr/sbin/chown -R root:wheel /System/Library/PrivateFrameworks//Accessibility*.framework"
#PurpleExec /usr/sbin/chown -- -R root:wheel /System/Library/PrivateFrameworks/AccessibilityUI.framework.dSYM
#PurpleExec /usr/sbin/chown -- -R root:wheel /System/Library/PrivateFrameworks/AccessibilityUIService.framework.dSYM

exit 0
fi
#*/
if [ "${CONFIGURATION}" = "Debug" ] && [ "${EFFECTIVE_PLATFORM_NAME}" = "-iphonesimulator" ]; then
osascript -e 'do shell script "
cd ${TARGET_BUILD_DIR}

# Sync the AX umbrella framework, and its real sub-frameworks
sudo rsync -av AccessibilityUIUtilities.framework* ${SDKROOT}/System/Library/PrivateFrameworks/
sudo rsync -av ZoomServices.framework* ${SDKROOT}/System/Library/PrivateFrameworks/
sudo rsync -av VoiceOverServices.framework* ${SDKROOT}/System/Library/PrivateFrameworks/
sudo rsync -av SpeakThisServices.framework* ${SDKROOT}/System/Library/PrivateFrameworks/
sudo rsync -av AXSpeakFingerManager.framework* ${SDKROOT}/System/Library/PrivateFrameworks/
sudo rsync -av AXGuestModeServices.framework* ${SDKROOT}/System/Library/PrivateFrameworks/
sudo rsync -av AccessibilityUI.framework* ${SDKROOT}/System/Library/PrivateFrameworks/
sudo rsync -av AccessibilityUIService.framework* ${SDKROOT}/System/Library/PrivateFrameworks/
sudo rsync -av AXSpringBoardServerInstance.framework* ${SDKROOT}/System/Library/PrivateFrameworks/
sudo rsync -av AXFrontBoardUtils.framework* ${SDKROOT}/System/Library/PrivateFrameworks/
sudo rsync -av SoundBoardAccessibility.framework* ${SDKROOT}/System/Library/PrivateFrameworks/

sudo rsync -av AccessibilityUtilities.framework*  VisualAlert.framework* UIAccessibility.framework* AXRuntime.framework* ${SDKROOT}/System/Library/PrivateFrameworks

sudo rsync -av AXActionSheetUIServer.axuiservice* VisualAlerts.bundle* AccessibilitySettingsLoader.bundle* HearingAidUIServer.axuiservice* ${SDKROOT}/System/Library/AccessibilityBundles
sudo rsync -av UIKit.axbundle* ${SDKROOT}/System/Library/AccessibilityBundles
sudo rsync -av libAccessibility.dylib* ${SDKROOT}/usr/lib
sudo rsync -av AXCoreUtilities.framework* /System/Library/PrivateFrameworks

sudo rsync -av UltronApp* ${SDKROOT}/AppleInternal/Applications
#    sudo rsync -av AccessibilityFrameworkUnitTests.octest* ${SDKROOT}/System/Library/AccessibilityBundles/UIKit.axbundle/
sudo rsync -av QuickSpeak.bundle* ${SDKROOT}/System/Library/AccessibilityBundles
sudo rsync -av AXSpeechImplementation.bundle* ${SDKROOT}/System/Library/AccessibilityBundles
sudo rsync -av libAXSpeechManager.dylib* ${SDKROOT}/usr/lib
sudo rsync -av libAXSafeCategoryBundle.dylib* ${SDKROOT}/usr/lib
sudo rsync -av SpeakThis.axuiservice* ${SDKROOT}/System/Library/AccessibilityBundles
sudo rsync -av SpeakThis.axuiservice* ${SDKROOT}/System/Library/AccessibilityBundles
sudo rsync -av StickyKeys.axuiservice* ${SDKROOT}/System/Library/AccessibilityBundles
sudo rsync -av TouchAccommodations.axuiservice* ${SDKROOT}/System/Library/AccessibilityBundles
sudo rsync -av AccessibilityDataMigration.migrator* ${SDKROOT}/System/Library/DataClassMigrators
sudo rsync -av AXElementInteractionUIServer.axuiservice* ${SDKROOT}/System/Library/AccessibilityBundles
sudo rsync -av AXElementInteraction.framework* ${SDKROOT}/System/Library/PrivateFrameworks/
sudo rsync -av AXElementInteractionTester* ${SDKROOT}/usr/local/bin
# sudo rsync -av *TapToRadar*.appex* ${SDKROOT}/System/Library/PrivateFrameworks/AccessibilityUtilities.framework/PlugIns/

rsync -av AXContainerManagerServer.axuiservice* ${SDKROOT}/System/Library/AccessibilityBundles
rsync -av AXContainerServices.framework* ${SDKROOT}/System/Library/PrivateFrameworks/

sudo rsync -av AXUIAutomationLibrary.bundle* ${SDKROOT}/AppleInternal/Library/Bundles/UIAutomation
sudo rsync -av Accessibility.assistantBundle* ${SDKROOT}/System/Library/Assistant/Plugins
#    rsync -av ${SRCROOT}/../../Scripts/HearingAidTests /usr/local/etc/
#    rsync -av ${SRCROOT}/../../Scripts/UITests/* /usr/local/etc/axscripts/
sudo rsync -av Accessibility*Module.bundle* ${SDKROOT}/System/Library/ControlCenter/Bundles

sudo rsync -Wav ${TARGET_BUILD_DIR}/axspeech ${SDKROOT}/usr/local/bin

xt=$?
if [ $xt -eq 0 ] || [ $xt -eq 23 ] ; then
echo Success: Synced products to simulator
else
echo Error: Could not sync AX frameworks to simulator. Is it connected? Wait, what?
fi

# fix up the permissions on AXUIServers root:wheel
echo Fixing permissions on AccessibilityUIService.framework
sudo /usr/sbin/chown -R root:wheel ${SDKROOT}/System/Library/PrivateFrameworks//Accessibility*.framework
#    sudo /usr/sbin/chown -R root:wheel ${SDKROOT}/System/Library/PrivateFrameworks/AccessibilityUI.framework.dSYM
#    sudo /usr/sbin/chown -R root:wheel ${SDKROOT}/System/Library/PrivateFrameworks/AccessibilityUIService.framework.dSYM
" with administrator privileges'
exit 0
fi
